# importing ultralytics
from ultralytics import YOLO

# loading the model
model = YOLO("yolov8m-cls.pt")

# Training the model
results = model.train(data='path/to/dataset', epochs=50, batch=16, imgsz=224, plots=True, save=True)

# Validate the model
results = model.val()