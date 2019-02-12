from darkflow.net.build import TFNet
import cv2
import matplotlib.pyplot as plt
# %config inlineBackend.figure_format = 'svg'
import numpy as np
import os

def load_images_from_folder(folder):
	images = []
	for filename in os.listdir(folder):
		img = cv2.imread(os.path.join(folder,filename))
		if img is not None:
		    images.append(img)
	return images



options = {
		"model": "cfg/tiny-yolo-voc-12c.cfg", 
		"load": 4000, 
		"threshold": 0.1,
		"GPU":1
		}

tfnet = TFNet(options)

# images = load_images_from_folder("./sample_img/*.jpg")

imgcv = cv2.imread("./dataset/test_images/000500.jpg")
# imgcv = cv2.cvtColor(imgcv,cv2.COLOR_BGR2RGB)
result = tfnet.return_predict(imgcv)
print(result)

for i in range(len(result)):
	t1 = (result[i]['topleft']['x'],result[i]['topleft']['y'])
	b1 = (result[i]['bottomright']['x'],result[i]['bottomright']['y'])
	label = (result[i]['label'])
	confidence = int(result[i]['confidence']*100)
	name = label + ' ' +  str(confidence)+'%'
	col = np.random.rand(3)*255
	imgcv = cv2.rectangle(imgcv,t1,b1,(col),10)
	imgcv = cv2.putText(imgcv,name,t1,cv2.FONT_HERSHEY_DUPLEX,3,(col),5)

plt.imshow(imgcv)
plt.show()
