YOLOv7 has been trained on the COCO [7] dataset. The COCO dataset has 80 classes. While it does have classes like "Car", "Traffic Light" and such that are relevant to road object detection, it also has irrerelevant classes like "toothbrush" and "Unbrella" to name a few. Therefore, our project adapts YOLOv7 for road object detection by training it with the BDD100K dataset.

BDD100K is one of the largest and most diverse driving datasets available to the public. It is an extensive collection of images and video captured from real-world driving scenarios, containing various weather conditions, lighting conditions, and urban environments. The dataset provides annotations for a wide range of objects, including cars, pedestrians, cyclists, traffic signs, and more. Specifically, we use the "BDD100K | 100K Images" and "BDD100K | Detection 2020 Labels" collections.

BDD100k has 10 classes. The **train**, **val**, **test** sets have 70K, 10K, 20K images. The **train** and **val** sets come with a .json file each, with the annotations.
The annotations need to be transformed to the YOLOv7 format. The YOLOv7 format is as follows:
- 1 .txt file per image.
- Within that .txt file, 1 line for each detected object class.
- Each detected object class is represented by its numeric class_ID, and bounding box: class_ID, x_centroid, y_centroid, width, height
- The centroids, width, and height are normalized using the image dimensions (1280x720)
