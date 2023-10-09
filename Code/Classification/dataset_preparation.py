"""
Preparaing Dataset in YOLOv8 Classification Format:

datasets:
        train:
            class-1:
                images...
            class-2:
                images...
        val:
            class-1:
                images...
            class-2:
                images...
"""

# Imporing Libraries

import splitfolders
import os
import shutil

""" Bleeding """

# Splitting bleeding folder into train and val datasets in ratio 0.8 and 0.2 respectively
input_folder = 'path/to/training_dataset/bleeding'
output_folder = 'path/to/output_folder/Classification/'

# Split the dataset into training and validation sets
splitfolders.ratio(input_folder, output_folder, seed=42, ratio=(.8, .2), group_prefix=None)

# Copying the images to bleeding category folders
src = '/content/Classifiication/train/Images/'
dst = '/content/Classifiication/train/bleeding/'
shutil.copytree(src, dst)

src = '/content/Classifiication/val/Images/'
dst = '/content/Classifiication/val/bleeding/'
shutil.copytree(src, dst)

# Removing the extra folders not required for classification
shutil.rmtree('/content/Classifiication/train/Images/')
shutil.rmtree('/content/Classifiication/train/Annotations/')
shutil.rmtree('/content/Classifiication/train/Bounding boxes/')
shutil.rmtree('/content/Classifiication/val/Images/')
shutil.rmtree('/content/Classifiication/val/Annotations/')
shutil.rmtree('/content/Classifiication/val/Bounding boxes/')


""" Non-Bleeding """

# Splitting non-bleeding folder into train and val datasets in ratio 0.8 and 0.2 respectively
input_folder = 'path/to/training_dataset/non-bleeding'
output_folder = 'path/to/output_folder/Classification/'

# Split the dataset into training and validation sets
splitfolders.ratio(input_folder, output_folder, seed=42, ratio=(.8, .2), group_prefix=None)

# Copying the images to non-bleeding category folders
src = '/content/Classifiication/train/images/'
dst = '/content/Classifiication/train/non-bleeding/'
shutil.copytree(src, dst)

src = '/content/Classifiication/val/images/'
dst = '/content/Classifiication/val/non-bleeding/'
shutil.copytree(src, dst)

# Removing the extra folders not required for classification
shutil.rmtree('/content/Classifiication/train/images/')
shutil.rmtree('/content/Classifiication/train/annotation/')
shutil.rmtree('/content/Classifiication/val/images/')
shutil.rmtree('/content/Classifiication/val/annotation/')