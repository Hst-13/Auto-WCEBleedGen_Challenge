# Auto-WCEBleedGen_Challenge

The Auto-WCEBleedGen challenge aims to provide an opportunity to develop, test and evaluate Artificial Intelligence (AI) models for automatic detection and classification of bleeding and non-bleeding frames extracted from Wireless Capsule Endoscopy (WCE) videos.

## Model Evaluation

#### Classification
| Model | Accuracy | Recall | F1-Score |
|----------|--------|----------|-------|
| <a href="Models">Yolov8m-cls</a> |    1     |   1    |     1    |

#### Detection (Box)
| Model | AP | mAP-50 | mAP50-95 |
|-------|----|--------|-------|
| <a href="Models">Yolov8n-seg<a> | 0.756  | 0.756 | 0.444 |

#### Segmentation (Mask)
| Model | AP | mAP-50 | mAP50-95 |
|-------|----|--------|-------|
| <a href="Models">Yolov8n-seg</a> | 0.69  | 0.69 | 0.31 |

## Validation Dataset

- ### Classification
  <img src="Best Images/Validation/Classification/img- (30).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Validation/Classification/img- (61).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Validation/Classification/img- (162).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Validation/Classification/img- (228).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Validation/Classification/img- (635).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Validation/Classification/img- (649).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Validation/Classification/img- (990).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Validation/Classification/img- (1042).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Validation/Classification/img- (1122).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Validation/Classification/img- (1213).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
- ### Detection
  <img src="Best Images/Validation/Segmentation/img- (30).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Validation/Segmentation/img- (61).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Validation/Segmentation/img- (162).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Validation/Segmentation/img- (228).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Validation/Segmentation/img- (635).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Validation/Segmentation/img- (649).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Validation/Segmentation/img- (990).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Validation/Segmentation/img- (1042).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Validation/Segmentation/img- (1122).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Validation/Segmentation/img- (1213).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
- ### Interpretability Plot (EigenCAM)
  - #### Classification
    <img src="Interpretabilty Plots/Validation/Classification/ip_img- (30).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Validation/Classification/ip_img- (61).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Validation/Classification/ip_img- (162).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Validation/Classification/ip_img- (228).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Validation/Classification/ip_img- (635).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Validation/Classification/ip_img- (649).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Validation/Classification/ip_img- (990).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Validation/Classification/ip_img- (1042).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Validation/Classification/ip_img- (1122).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Validation/Classification/ip_img- (1213).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  - #### Segmentation
    <img src="Interpretabilty Plots/Validation/Segmentation/ip_img- (30).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Validation/Segmentation/ip_img- (61).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Validation/Segmentation/ip_img- (162).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Validation/Segmentation/ip_img- (228).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Validation/Segmentation/ip_img- (635).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Validation/Segmentation/ip_img- (649).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Validation/Segmentation/ip_img- (990).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Validation/Segmentation/ip_img- (1042).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Validation/Segmentation/ip_img- (1122).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Validation/Segmentation/ip_img- (1213).png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    
## Testing Dataset 1
<a href="Labels/test1_classification_labels.xlsx">Test Dataset 1 Predicted Classification Labels</a> <br>
<a href="Labels/Test1_Segmentation_Masks/">Test Dataset 1 Predicted Segmentation Masks</a>
- ### Classification
  <img src="Best Images/Test Dataset 1/Classification/A0021.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Test Dataset 1/Classification/A0036.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Test Dataset 1/Classification/A0038.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Test Dataset 1/Classification/A0046.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Test Dataset 1/Classification/A0047.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
- ### Segmentation
  <img src="Best Images/Test Dataset 1/Segmentation/A0021.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Test Dataset 1/Segmentation/A0036.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Test Dataset 1/Segmentation/A0038.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Test Dataset 1/Segmentation/A0046.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Test Dataset 1/Segmentation/A0047.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
- ### Interpretability Plot (EigenCAM)
  - #### Classification
    <img src="Interpretabilty Plots/Test Dataset 1/Classification/ip_A0021.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Test Dataset 1/Classification/ip_A0036.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Test Dataset 1/Classification/ip_A0038.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Test Dataset 1/Classification/ip_A0046.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Test Dataset 1/Classification/ip_A0047.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  - #### Segmentation
    <img src="Interpretabilty Plots/Test Dataset 1/Segmentation/ip_A0021.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Test Dataset 1/Segmentation/ip_A0036.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Test Dataset 1/Segmentation/ip_A0038.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Test Dataset 1/Segmentation/ip_A0046.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Test Dataset 1/Segmentation/ip_A0047.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">

## Testing Dataset 2
<a href="Labels/test2_classification_labels.xlsx">Test Dataset 2 Predicted Classification Labels</a> <br>
<a href="Labels/Test2_Segmentation_Masks/">Test Dataset 2 Predicted Segmentation Masks</a><br>
- ### Classification
  <img src="Best Images/Test Dataset 2/Classification/A0051.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Test Dataset 2/Classification/A0450.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Test Dataset 2/Classification/A0500.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Test Dataset 2/Classification/A0507.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Test Dataset 2/Classification/A0550.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
- ### Segmentation                                             
  <img src="Best Images/Test Dataset 2/Segmentation/A0051.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Test Dataset 2/Segmentation/A0450.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Test Dataset 2/Segmentation/A0500.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Test Dataset 2/Segmentation/A0507.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  <img src="Best Images/Test Dataset 2/Segmentation/A0550.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
- ### Interpretability Plot (EigenCAM)
  - #### Classification
    <img src="Interpretabilty Plots/Test Dataset 2/Classification/ip_A0051.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Test Dataset 2/Classification/ip_A0450.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Test Dataset 2/Classification/ip_A0500.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Test Dataset 2/Classification/ip_A0507.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Test Dataset 2/Classification/ip_A0550.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
  - #### Segmentation
    <img src="Interpretabilty Plots/Test Dataset 2/Segmentation/ip_A0051.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Test Dataset 2/Segmentation/ip_A0450.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Test Dataset 2/Segmentation/ip_A0500.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Test Dataset 2/Segmentation/ip_A0507.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">
    <img src="Interpretabilty Plots/Test Dataset 2/Segmentation/ip_A0550.png" alt="Alt text" style="display: inline-block; margin: 0 auto; width: 128px">

## Codes
- <a href="Code/Classification/">Classification Code</a>
- <a href="Code/Segmentation/">Segmentation Code</a>
- <a href="Code/interpretability_plots_using_eigen_cam.py/">Interpretability Plot</a>
