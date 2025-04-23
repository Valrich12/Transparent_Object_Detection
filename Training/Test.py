from ultralytics import YOLO
import torch
model = YOLO('transparentS200ebN.pt')
results = model.predict(source=0,show=True,save = False, stream_buffer = True,conf = 0.65)