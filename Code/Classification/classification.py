# importing ultralytics
from ultralytics import YOLO

# loading the model
model = YOLO("yolov8m-cls.pt")

# Training the model
results = model.train(data='path/to/dataset', epochs=100, batch=16, imgsz=224, plots=True, save=True)

# Validate the model
results = model.val()

# Load a best.pt model
model = YOLO('path/to/best_model_file')

# Define path to directory containing images and videos for inference
source = 'path/to/source_dir'

# Run inference on the source
results = model(source, stream=True, name=name_of_output_folder, save=True, save_txt=True, save_conf=True)

""""
Using CLI Method (On Google Colab):

#Training
!yolo classify train data=path/to/data.yaml model=yolov8m-cls.pt name=name_of_output_folder epochs=100 batch=16 imgsz=224 save=True plots=True max_det=10 save_conf=True

#Validation
!yolo classify val model=path/to/best_model data=path/to/data.yaml name=name_of_output_folder

#Testing
!yolo classify predict model=path/to/model source=path/to/source_dir name=name_of_output_folder save=True

"""