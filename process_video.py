import numpy as np
import cv2
import time
import matplotlib.pyplot as plt
from darkflow.net.build import TFNet

option = {
	'model' : 'cfg/yolo.cfg',
	'load': 'bin/yolov2.weights',
	'threshold':0.3
}

tfnet = TFNet(option)
capture = cv2.VideoCapture('Hitman.mp4')
colors = [tuple(255*np.random.rand(3)) for i in range(15)]

while(capture.isOpened()):
	stime = time.time()
	ret, frame = capture.read()
	results = tfnet.return_predict(frame)
	if ret:
		for color, result in zip(colors,results):
			tl = (result['topleft']['x'],result['topleft']['y'])
			br = (result['bottomright']['x'],result['bottomright']['y'])
			label = result['label']
			frame = cv2.rectangle(frame,tl,br,color,6)
			frame = cv2.putText(frame,label,tl,cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
		cv2.imshow('frame',frame)
		print('FPS {:.1f}'.format(1/(time.time()-stime)))
		if cv2.waitKey(1)&0xFF == ord('q'):
			break
	else:
		capture.release()
		cv2.destroyAllWindows()
		break