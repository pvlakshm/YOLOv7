def category_string_to_classID(category_string):
  bdd_object_detectionb_classes = {
      "pedestrian"   : 0,
      "rider"        : 1,
      "car"          : 2,
      "truck"        : 3,
      "bus"          : 4,
      "train"        : 5,
      "motorcycle"   : 6,
      "bicycle"      : 7,
      "traffic light": 8,
      "traffic sign" : 9
  }

  class_ID = bdd_object_detectionb_classes[category_string]
  return class_ID


'''
Yolo format is as follows:
1 file per image.
Within that file, 1 line for each detected object. Each detected object will
be represented by its numberic COCO_ID, and its bounding box as follows:
  COCO_ID, x_centroid, y_centroid, width, height

The centroids and the width and height are normalized using the immage dimensions
'''

import os
import json
import sys

def bdd_to_yolov7(bdd_dataset_path, output_path, image_width, image_height):
  # Create output directory if it doesn't exist
  os.makedirs(output_path, exist_ok = True)

  # Load BDD dataset
  with open(bdd_dataset_path, 'r') as file:
    bdd_dataset = json.load(file)

  # Process each image in the dataset
  for image_data in bdd_dataset:
    # Create a named YOLO annotation file
    image_name    = image_data['name']
    yolo_filename = os.path.splitext(image_name)[0] + '.txt'
    yolo_filepath = os.path.join(output_path, yolo_filename)
    yolo_file     = open(yolo_filepath, 'w')

    try:
      annotations = image_data['labels']
      for annotation in annotations:
        id = category_string_to_classID(annotation['category'])
        x1 = annotation['box2d']['x1']
        y1 = annotation['box2d']['y1']
        x2 = annotation['box2d']['x2']
        y2 = annotation['box2d']['y2']
        width  = (x2 - x1)
        height = (y2 - y1)

        # normalize using the iamge dimensions,
        x_centroid = (x1 + width/2) / image_width
        y_centroid = (y1 + height/2) / image_height
        width      = width / image_width
        height     = height / image_height

        # Write YOLO annotation to file
        yolo_line = f"{id} {x_centroid} {y_centroid} {width} {height}\n"
        yolo_file.write(yolo_line)
    except:
      pass

  print("Conversion completed successfully.")

BDD_DATASET_FILE   = sys.argv[1]
OUTPUT_FOLDER_PATH = sys.argv[2]
IMAGE_WIDTH        = 1280
IMAGE_HEIGHT       = 720

bdd_to_yolov7(BDD_DATASET_FILE, OUTPUT_FOLDER_PATH, IMAGE_WIDTH, IMAGE_HEIGHT)