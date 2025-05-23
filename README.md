# YOLOv7 - Road Object Detection
Given a large heterogeneous driving dataset of images, the goal is to train a model for road object detection - i.e., to accurately and automatically **classify**, **detect**, and **track** objects present therein.

**Object Classification** involves identifying and labelling specific classes in the image, such as "car", "pedestrian", or "traffic light".  
**Object Detection** then accurately localizes their positions within the image.  
Finally, **Object Tracking** follows the objects over time within a sequence of frames.

The implementation is divided along the following statges:

1, [Data Preparation](DataPreparation/README.md)  
2. [Detection](Detection/README.md)  
3. [Deployment](Deployment/README.md)  
4. [Multi-Object Tracking](MOT/README.md)  

## Experimental Setup
Environment: Google Colab Pro+  
Hardware accelerator: A100 GPU  
Shape: High-RAM 

## References
**[1]** Wong, Kin-Yiu, Yuhang Chen, Zhiqiang Liu, Jianwei Zhang, and Dahua Lin. "YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors." arXiv preprint arXiv:2207.02696 (2022).  
**[2]** Liu, Wei, et al. "SSD: Single Shot MultiBox Detector." arXiv preprint arXiv:1512.02325 (2015).  
**[3]** Girshick, Ross, et al. "Rich Feature Hierarchies for Accurate Object Detection and Semantic Segmentation." arXiv preprint arXiv:1311.2524 (2014).  
**[4]** Ren, Shaoqing, Kaiming He, Ross Girshick, and Jian Sun. "Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks." arXiv preprint arXiv:1506.01497 (2015).  
**[5]** Lin, T.-Y., P. Goyal, R. B. Girshick, K. He, and P. Dollár. "Focal Loss for Dense Object Detection." arXiv preprint arXiv:1708.02002 (2017).  
**[6]** Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays, Pietro Perona, Deva Ramanan, Radek Girshick, Christoph Dollar, and Ross Girshick. "Microsoft COCO: Common Objects in Context." In European Conference on Computer Vision (ECCV), 2014.  
**[7]** Yu, Fisher, et al. "Berkeley DeepDrive (BDD) Dataset." 2018. https://bdd-data.berkeley.edu/.  
**[8]** Wong, Kin-Yiu. "YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors." 2022. https://github.com/WongKinYiu/yolov7.  
