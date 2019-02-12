# Object-Detection-in-Floor-Plan-Images
Detection of Objects in a Floor Plan and Architectural Images

Today there are many models available for doing object detection recognition in an image.
Like RCNN, fast RCNN, faster RCNN, mask RCNN, Yolo, SSD etc.
all of them are developed and configured for natural images. In this project we are working on
document images of floor plans. In a floor plan image, we have objects like dining table, sofa,
sink, etc. we used the yolo and faster RCNN for object detection.

we used darkflow implementation of yolo https://github.com/thtrieu/darkflow and
we used https://github.com/kbardool/keras-frcnn for frcnn

DATASET-

SESYD, “http://mathieu.delalandre.free.fr/projects/sesyd/symbols/floorplans.html”

ROBIN dataset, [online] Available: “https://github.com/gesstalt/ROBIN.git”

in addition we collected dataset by web scraping from some websites like “architecturalhouseplans.com” and
“houseplans.com”.

YOLO-

download the darkflow yolo from above given link.

download bin, cfg, and dataset folder from above and add them to downloaded darkflow repository.

we trained the model. to train your the model you can run the command-

python flow --model cfg/tiny-yolo-voc-3c.cfg --load bin/tiny-yolo-voc.weights --train --annotation dataset/train_annotation --dataset dataset/train_images

to predict the image run the predict_img.py file (you can prefer to change in option like model, load values etc.)

faster RCNN-

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


