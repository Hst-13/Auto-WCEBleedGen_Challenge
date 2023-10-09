from ultralytics import YOLO

model = YOLO("yolov8m-cls.pt")

# Train the model
results = model.train(data='path/to/dataset', epochs=100, batch=16, imgsz=224, plots=True, save=True)

# Validate the model
results = model.val()