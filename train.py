from ultralytics import YOLO

# Load a pretrained YOLOv8 model (Nano version for faster training)
model = YOLO('yolo11m.pt')

# Start training
results = model.train(
    data='data.yaml',    # path to dataset config file
    epochs=50,           # number of epochs
    imgsz=640,           # input image size
    batch=8,             # batch size (adjust based on your GPU)
    name='profesor_mario_yolov11'  # output folder name for this training run
)
