# importing ultralytics
from ultralytics import YOLO

# loading the model
model=YOLO("yolov8n-seg.pt")

# Training the model
results = model.train(data='path/to/dataset/data.yaml', epochs=100, batch=16, imgsz=224, plots=True, save=True, retina_masks=True)

#Validate the model
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
!yolo segment train data=path/to/data.yaml model=yolov8n-seg.pt name=name_of_output_folder epochs=100 batch=16 imgsz=224 save=True plots=True conf=0.10 iou=0.6 max_det=10 save_conf=True retina_masks=True

#Validation
!yolo segment val model=path/to/best_model data=path/to/data.yaml name=name_of_output_folder

#Testing
!yolo segment predict model=path/to/model source=path/to/source_dir name=name_of_output_folder save=True

"""