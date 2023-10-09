"""
Preparaing Dataset in YOLOv8 Segmentation Format:

datasets:
        train:
            image1
            image1.txt
            image2
            image2.txt
            .
            .
            .
        val:
            image1
            image1.txt
            image2
            image2.txt
            .
            .
            .
"""

# Imporing Libraries

import splitfolders
import os
import shutil
import cv2

# Splitting bleeding folder into train and val datasets in ratio 0.8 and 0.2 respectively
input_folder = 'path/to/training_dataset/bleeding'
output_folder = 'path/to/split_folder/Segmentation/'

# Split the dataset into training and validation sets
splitfolders.ratio(input_folder, output_folder, seed=42, ratio=(.8, .2), group_prefix=None)

# Creating directries for storing txt file containing polygon masks
os.mkdir('path/to/split_folder/Segmentation/train/labels/')
os.mkdir('path/to/split_folder/Segmentation/val/labels/')

# Method for extracting polygon coordinates from given binary masks
def make_polygons(input_dir, output_dir):
  for j in os.listdir(input_dir):
      image_path = os.path.join(input_dir, j)
      # load the binary mask and get its contours
      mask = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
      _, mask = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY)

      H, W = mask.shape
      contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

      # convert the contours to polygons
      polygons = []
      for cnt in contours:
          if cv2.contourArea(cnt) > 200:
              polygon = []
              for point in cnt:
                  x, y = point[0]
                  polygon.append(x / W)
                  polygon.append(y / H)
              polygons.append(polygon)

      # print the polygons in txt files
      with open('{}.txt'.format(os.path.join(output_dir, j)[:-4]), 'w') as f:
          for polygon in polygons:
              for p_, p in enumerate(polygon):
                  if p_ == len(polygon) - 1:
                      f.write('{}\n'.format(p))
                  elif p_ == 0:
                      f.write('0 {} '.format(p))
                  else:
                      f.write('{} '.format(p))

          f.close()

# passing the input directory and output directory
input_dir = 'path/to/split_folder/Segmentation/train/Annotations/'
output_dir = 'path/to/split_folder/Segmentation/train/labels/'
make_polygons(input_dir, output_dir)

# passing the input directory and output directory
input_dir = 'path/to/split_folder/Segmentation/val/Annotations/'
output_dir = 'path/to/split_folder/Segmentation/val/labels/'
make_polygons(input_dir, output_dir)

src = 'path/to/split_folder/Segmentation/'

# Copying the files from Bleeding Images and labels folder to training and validation folder
for folder in ['Images/', 'labels/']:
  for mode in ['train/', 'val/']:
    for f in os.listdir(src+mode+folder):
      shutil.copy(src+mode+folder+f, src+mode+f)

# Renaming the polygon masks files as same as the corresponding image
def rename_labels(folder_path):
    for filename in os.listdir(folder_path):
        if filename.startswith("ann- "):
            new_filename = filename.replace("ann- ", "img- ")
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

# passing the folder path for renaming
folder_path = "path/to/split_folder/Segmentation/train/"
rename_labels(folder_path)
folder_path = "path/to/split_folder/Segmentation/val/"
rename_labels(folder_path)

# Removing the extra folders not required for segmentation
shutil.rmtree('path/to/split_folder/Segmentation/train/Bounding boxes/')
shutil.rmtree('path/to/split_folder/Segmentation/val/Bounding boxes/')
shutil.rmtree('path/to/split_folder/Segmentation/train/Annotations/')
shutil.rmtree('path/to/split_folder/Segmentation/val/Annotations/')
shutil.rmtree('path/to/split_folder/Segmentation/train/Images/')
shutil.rmtree('path/to/split_folder/Segmentation/val/Images/')
shutil.rmtree('path/to/split_folder/Segmentation/train/labels/')
shutil.rmtree('path/to/split_folder/Segmentation/val/labels/')
