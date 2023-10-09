import splitfolders
import os
import shutil

"""
Bleeding

"""

input_folder = 'path/to/training_dataset/bleeding'
output_folder = 'path/to/output_folder/Classification/'

# Split the dataset into training and validation sets
splitfolders.ratio(input_folder, output_folder, seed=42, ratio=(.8, .2), group_prefix=None)

src = '/content/Classifiication/train/Images/'
dst = '/content/Classifiication/train/bleeding/'
shutil.copytree(src, dst)

src = '/content/Classifiication/val/Images/'
dst = '/content/Classifiication/val/bleeding/'
shutil.copytree(src, dst)

shutil.rmtree('/content/Classifiication/train/Images/')
shutil.rmtree('/content/Classifiication/train/Annotations/')
shutil.rmtree('/content/Classifiication/train/Bounding boxes/')
shutil.rmtree('/content/Classifiication/val/Images/')
shutil.rmtree('/content/Classifiication/val/Annotations/')
shutil.rmtree('/content/Classifiication/val/Bounding boxes/')

"""
Non-Bleeding

"""

input_folder = 'path/to/training_dataset/non-bleeding'
output_folder = 'path/to/output_folder/Classification/'

# Split the dataset into training and validation sets
splitfolders.ratio(input_folder, output_folder, seed=42, ratio=(.8, .2), group_prefix=None)

src = '/content/Classifiication/train/images/'
dst = '/content/Classifiication/train/non-bleeding/'
shutil.copytree(src, dst)

src = '/content/Classifiication/val/images/'
dst = '/content/Classifiication/val/non-bleeding/'
shutil.copytree(src, dst)

shutil.rmtree('/content/Classifiication/train/images/')
shutil.rmtree('/content/Classifiication/train/annotation/')
shutil.rmtree('/content/Classifiication/val/images/')
shutil.rmtree('/content/Classifiication/val/annotation/')