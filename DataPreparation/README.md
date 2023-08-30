YOLOv7 has been trained on the COCO [7] dataset. The COCO dataset has 80 classes. While it does have classes like "Car", "Traffic Light" and such that are relevant to raod object detection, it also has irrerelevant classes like "toothbrush"a and :Unbrella" to name a few. Therefore, our project adapts YOLOv7 for road object detection by training it with the BDD100K dataset.

BDD100K is one of the largest and most diverse driving datasets available to the public. It has 10 classes. The train, val, test sets have 70%, 10%, 20% images. The train and val sets come with a .json file each, with the annotations.
The annotations need to be transformed to the YOLOv7 format. The YOLOv7 format is as follows:
- 1 .txt file per image.
- Within that .txt file, 1 line for each detected object class.
- Each detected object class is represented by its numeric class_ID, and bounding box: class_ID, x_centroid, y_centroid, width, height
- The centroids, width, and height are normalized using the image dimensions (1280x720)
