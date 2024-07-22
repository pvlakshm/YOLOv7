YOLOv7 has been trained on the COCO dataset [[6]](https://github.com/pvlakshm/YOLOv7/tree/main?tab=readme-ov-file#references). The COCO dataset has 80 classes. While it does have classes like "Car", "Traffic Light" and such that are relevant to road object detection, it also has irrerelevant classes like "toothbrush" and "Unbrella" to name a few. Therefore, our project adapts YOLOv7 for road object detection by training it with the BDD100K dataset [[7]](https://github.com/pvlakshm/YOLOv7/tree/main?tab=readme-ov-file#references).

# BDD100K
BDD100K is one of the largest and most diverse driving datasets available to the public. It is an extensive collection of images and video captured from real-world driving scenarios, containing various weather conditions, lighting conditions, and urban environments. The dataset provides annotations for a wide range of objects, including cars, pedestrians, cyclists, traffic signs, and more. Specifically, we use the **"BDD100K | 100K Images"** and **"BDD100K | Detection 2020 Labels"** collections.

BDD100k has 10 classes. The **train**, **val**, **test** sets have 70K, 10K, 20K images. The **train** and **val** sets come with a .json file each, with the annotations.
The annotations need to be transformed to the YOLOv7 format. The YOLOv7 format is as follows:
- 1 .txt file per image.
- Within that .txt file, 1 line for each detected object class.
- Each detected object class is represented by its numeric class_ID, and bounding box: class_ID, x_centroid, y_centroid, width, height
- The centroids, width, and height are normalized using the image dimensions (1280x720)

# Transforming the dataset to YOLOv7 format
## Usage
**```python tranform.py <arg1> <arg2>```**  
  
**```arg1```** is the filename of a BDD100K json file  
**```arg2```** is the name of a folder where the .txt files in YOLOv7 format will be created.

Sample  
**```python tranform.py det_train.json transformed```**

## Removing images without annotaions
As it turns out there are 137 images in the dataset with missing annotatations. We need to find out those images and remove them from the dataset.
