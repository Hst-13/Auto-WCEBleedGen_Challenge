import splitfolders
import os
import shutil
import cv2

input_folder = 'path/to/training_dataset/bleeding'
output_folder = 'path/to/output_folder/Segmentation/'

# Split the dataset into training and validation sets
splitfolders.ratio(input_folder, output_folder, seed=42, ratio=(.8, .2), group_prefix=None)

import cv2

os.mkdir('/content/Segmentation/train/labels/')
os.mkdir('/content/Segmentation/val/labels/')

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

      # print the polygons
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

input_dir = '/content/Segmentation/train/Annotations/'
output_dir = '/content/Segmentation/train/labels/'
make_polygons(input_dir, output_dir)

input_dir = '/content/Segmentation/val/Annotations/'
output_dir = '/content/Segmentation/val/labels/'
make_polygons(input_dir, output_dir)

src = '/content/Segmentation/'

for folder in ['Images/', 'labels/']:
  for mode in ['train/', 'val/']:
    for f in os.listdir(src+mode+folder):
      shutil.copy(src+mode+folder+f, src+mode+f)

def rename_labels(folder_path):
    for filename in os.listdir(folder_path):
        if filename.startswith("ann- "):
            new_filename = filename.replace("ann- ", "img- ")
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

folder_path = "/content/Segmentation/train/"
rename_labels(folder_path)
folder_path = "/content/Segmentation/val/"
rename_labels(folder_path)

shutil.rmtree('/content/Segmentation/train/Bounding boxes/')
shutil.rmtree('/content/Segmentation/val/Bounding boxes/')
shutil.rmtree('/content/Segmentation/train/Annotations/')
shutil.rmtree('/content/Segmentation/val/Annotations/')
shutil.rmtree('/content/Segmentation/train/Images/')
shutil.rmtree('/content/Segmentation/val/Images/')
shutil.rmtree('/content/Segmentation/train/labels/')
shutil.rmtree('/content/Segmentation/val/labels/')
