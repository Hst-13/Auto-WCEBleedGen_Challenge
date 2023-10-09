"""
Interpretability Plot using Eigen CAM

Set-up environment:
    !pip install ultralytics
    !pip install ttach

    !git clone https://github.com/rigvedrs/YOLO-V8-CAM.git
    %cd /content/YOLO-V8-CAM

"""

#Import Libraries

import ultralytics
from ultralytics import YOLO
import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')
import torch
import cv2
import numpy as np
import matplotlib.pyplot as plt
import requests
import torchvision.transforms as transforms
from PIL import Image
import io
from yolo_cam.eigen_cam import EigenCAM
from yolo_cam.utils.image import show_cam_on_image, scale_cam_image

# Load the model
model = YOLO('path/to/stored_model')

# Sorce of Images
src = '/content/best_imgs/TD2/'

# Loop for plotting and saving the interpretability plots
for f in os.listdir(src):
  img = cv2.imread(src+f)
  rgb_img = img.copy()
  img = np.float32(img) / 255
  target_layers =[model.model.model[-4]]
  cam = EigenCAM(model, target_layers,task='cls') # task='cls' for Classification and task='od' for Segmentation
  grayscale_cam = cam(rgb_img)[0, :, :]
  cam_image = show_cam_on_image(img, grayscale_cam, use_rgb=True)
  plt.imshow(cam_image)
  plt.title(f)
  plt.savefig('path/to/dirctory/interpretability_plots/ip_'+f, dpi='figure') # Saving the plot
  plt.show()
