# install
!pip install ultralytics

# train
yolo detect train data=data.yml model=yolo11m.pt epochs=100 imgsz=640

# resume
yolo detect train resume model=bestNmario600.pt data=data.yml epochs=100 imgsz=640
