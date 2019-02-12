# Object-Detection-in-Floor-Plan-Images
Detection of Objects in a Floor Plan and Architectural Images

Today there are many models available for doing object detection recognition in an image.
Like RCNN, fast RCNN, faster RCNN, mask RCNN, Yolo, SSD etc.
all of them are developed and configured for natural images. In this project we are working on
document images of floor plans. In a floor plan image, we have objects like dining table, sofa,
sink, etc. we used the yolo and faster RCNN for object detection.

we used darkflow implementation of yolo https://github.com/thtrieu/darkflow and
we used https://github.com/kbardool/keras-frcnn for frcnn

Dataset-

SESYD, “http://mathieu.delalandre.free.fr/projects/sesyd/symbols/floorplans.html”\n
ROBIN dataset, [online] Available:​ ​ “https://github.com/gesstalt/ROBIN.git”\n
in addition we collected dataset by web scraping from some websites like “architecturalhouseplans.com” and
“houseplans.com”.

yolo-
download the darkflow yolo from above given link.
download bin, cfg, and dataset folder from above and add them to downloaded darkflow repository.
we trained the model. to train your the model you can run the command-
python flow --model cfg/tiny-yolo-voc-3c.cfg --load bin/tiny-yolo-voc.weights --train --annotation dataset/train_annotation --dataset dataset/train_images


