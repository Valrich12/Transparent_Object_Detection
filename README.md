# Transparent Object Detection using YOLOv11

This repository contains a computer vision project focused on detecting transparent objects using a fine-tuned **YOLOv11** model. The project is part of an exploration into modern object detection techniques applied to challenging visual scenarios, such as low contrast and see-through surfaces.

## Project Overview

Transparent object detection remains a complex task in computer vision due to the lack of clear edges, reflections, and background blending. In this project, we fine-tune **YOLOv11**, a state-of-the-art real-time object detection model, to recognize transparent items such as glassware, bottles, and plastic containers.

## Dataset

The model is trained and evaluated using the **TransLAB** dataset, which provides high-quality, annotated images of transparent objects under various conditions.

📦 **Dataset**: [TransLAB: A Transparent Object Dataset](https://xieenze.github.io/projects/TransLAB/TransLAB.html)

The dataset includes:
- Pixel-level annotations
- A variety of lighting and background conditions

## Features

- ✅ Fine-tuned YOLOv11 on transparent objects
- ✅ High precision bounding box predictions
- ✅ Support for real-time inference
- ✅ Evaluation with mAP and IoU metrics

## Technologies Used

- Python 3
- PyTorch
- YOLOv11
- OpenCV
- NumPy
- Matplotlib



