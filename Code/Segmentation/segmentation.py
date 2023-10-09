# importing ultralytics
from ultralytics import YOLO

# loading the model
model=YOLO("yolov8n-seg.pt")

# Training the model
results = model.train(data='path/to/dataset/data.yaml', epochs=100, batch=16, imgsz=224, plots=True, save=True, retina_masks=True)

#Validate the model
results = model.val()