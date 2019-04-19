# Object-Detection-in-Floor-Plan-Images
Detection of Objects in a Floor Plan and Architectural Images

There are few models available for doing object detection recognition in an image.
Like RCNN, fast RCNN, faster RCNN, mask RCNN, Yolo, SSD etc.
all of them are developed and configured for natural images. In this project we are working on
document images of floor plans. In a floor plan image, we have objects like dining table, sofa,
sink, etc. 
<p>we used the yolo and faster RCNN for object detection.</p>

<p>used darkflow implementation of yolo https://github.com/thtrieu/darkflow<br>
  used https://github.com/kbardool/keras-frcnn for frcnn</p>


<b>DATASET-</b>

SESYD, “http://mathieu.delalandre.free.fr/projects/sesyd/symbols/floorplans.html”

ROBIN dataset, [online] Available: “https://github.com/gesstalt/ROBIN.git”

in addition we collected dataset by web scraping from some websites like “architecturalhouseplans.com” and
“houseplans.com”.

<b>YOLO-</b>

download the darkflow yolo from above given link.

download weight, cfg files from https://pjreddie.com/darknet/yolo/ there are plenty available and download the one which you need and add them to downloaded darkflow repository in bin and cfg directories respectively.

download dataset from above links or you can use your own and addd them to dataset repository in downloaded darkflow repositor.

<b>TRAINING</b>

<i>assume that you want to use tiny-yolo cfg for training</i>

1. create a copy of configuration file tiny-yolo-voc.cfg and rename it to tiny-yolo-voc-12c.cfg (12c refer to the number of objects or classes we are identifying ) leave the original file unchanged.


To train your the model you can run the command-

python flow --model cfg/tiny-yolo-voc-3c.cfg --load bin/tiny-yolo-voc.weights --train --annotation dataset/train_annotation --dataset dataset/train_images

to predict the image run the predict_img.py file (you can prefer to change in option like model, load values etc.)

faster RCNN-
download the frcnn folder from above
to train model run command-

python train_frcnn.py -o simple -p train.txt

to test model run command-  
python test_frcnn.py -p test_images

Results-

YOLO-
object detected and  accuracy achieved
![](images/yolo_img_result1.png)

![](images/mAP.png)

faster FRCNN-
object detected and accuracy achieved
![](images/Frcnn_img_results1.png)


![](images/frcc_mAP.png)


