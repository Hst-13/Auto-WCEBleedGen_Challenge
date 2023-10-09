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
output_folder = 'path/to/split_folder/Classification/'

# Split the dataset into training and validation sets
splitfolders.ratio(input_folder, output_folder, seed=42, ratio=(.8, .2), group_prefix=None)

# Copying the images to bleeding category folders
src = 'path/to/split_folder/Classifiication/train/Images/'
dst = 'path/to/split_folder/Classifiication/train/bleeding/'
shutil.copytree(src, dst)

src = 'path/to/split_folder/Classifiication/val/Images/'
dst = 'path/to/split_folder/Classifiication/val/bleeding/'
shutil.copytree(src, dst)

# Removing the extra folders not required for classification
shutil.rmtree('path/to/split_folder/Classifiication/train/Images/')
shutil.rmtree('path/to/split_folder/Classifiication/train/Annotations/')
shutil.rmtree('path/to/split_folder/Classifiication/train/Bounding boxes/')
shutil.rmtree('path/to/split_folder/Classifiication/val/Images/')
shutil.rmtree('path/to/split_folder/Classifiication/val/Annotations/')
shutil.rmtree('path/to/split_folder/Classifiication/val/Bounding boxes/')


""" Non-Bleeding """

# Splitting non-bleeding folder into train and val datasets in ratio 0.8 and 0.2 respectively
input_folder = 'path/to/training_dataset/non-bleeding'
output_folder = 'path/to/split_folder/Classification/'

# Split the dataset into training and validation sets
splitfolders.ratio(input_folder, output_folder, seed=42, ratio=(.8, .2), group_prefix=None)

# Copying the images to non-bleeding category folders
src = 'path/to/split_folder/Classifiication/train/images/'
dst = 'path/to/split_folder/Classifiication/train/non-bleeding/'
shutil.copytree(src, dst)

src = 'path/to/split_folder/Classifiication/val/images/'
dst = 'path/to/split_folder/Classifiication/val/non-bleeding/'
shutil.copytree(src, dst)

# Removing the extra folders not required for classification
shutil.rmtree('path/to/split_folder/Classifiication/train/images/')
shutil.rmtree('path/to/split_folder/Classifiication/train/annotation/')
shutil.rmtree('path/to/split_folder/Classifiication/val/images/')
shutil.rmtree('path/to/split_folder/Classifiication/val/annotation/')