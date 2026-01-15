# Draw-It-Up: An Online Teaching Tool for Virtual Drawing and Writing

## Overview

**Draw-It-Up** is an interactive computer vision tool built using **OpenCV** and **CVZone** for real-time **hand tracking** and **finger counting**. The tool allows users to draw and erase on a virtual canvas using only their fingers, providing an intuitive way to interact with a virtual environment.

This project uses **CVZone** as a wrapper for **MediaPipe** for hand tracking and gesture recognition, ensuring smooth performance on Windows where direct **MediaPipe** integration may have compatibility issues with Python 3.13.

Perfect for teachers as an Online Teaching Tool where they can Virtually write or draw their concepts along with their Web Cam feed to increase interaction and understanding.

## Features

- **Hand Tracking**: Real-time detection and tracking of hand gestures using your webcam.
- **Finger Counting**: Recognizes the number of fingers raised, mapping it to specific actions.
- **Drawing & Erasing**: Use hand gestures to draw and erase on a canvas.
- **Interactive Feedback**: Immediate visual feedback for teaching or interactive learning.

## Technologies

- **OpenCV**: For image processing and computer vision tasks.
- **CVZone**: A wrapper around MediaPipe that simplifies hand tracking in Python.
- **MediaPipe**: A cross-platform framework for multimodal machine learning pipelines.
- **Python**: Backend logic to handle hand tracking and gesture recognition.

## How It Works

1. **Hand Tracking**: The system detects your hand using **CVZone** and **MediaPipe**'s hand tracking model, identifying key points like fingers and palm.
2. **Finger Counting**: The number of fingers raised is counted and mapped to different actions such as drawing and Selecting. Two fingers together are used for selecting various colours and the eraser option, whereas an extended index finger allows for drawing seamlessly.
3. **Drawing/Erasing**: The system allows you to draw or erase on a virtual canvas based on the detected gestures.

## Usage

Once you run the script (`draw_it_up_app.py`), the webcam feed will open, and the system will detect your hand movements. Here's how you can interact with it:

1. **Hand Tracking**: The system tracks your hand in real-time.
2. **Finger Counting**: The system recognizes the number of fingers raised.
3. **Drawing**: Raise the index finger allows for drawing or writing(Default colour is Red). Once the selection is changed to eraser you may use the same index finger to erase previously made drawings/write-ups.
4. **Selecting**: Two fingers raised together allow for selecting the various colour and eraser option from the menu bar.


### Example Finger Mapping:
- **1 Finger**: Activate drawing mode.
- **2 Fingers**: Activate selecting mode.
- **Other combinations**: Can be customized for different actions (like changing brush size).

### Output Screenshots
**Drawing with default colour - Red**

<img width="1593" height="931" alt="Screenshot 2026-01-15 172901" src="https://github.com/user-attachments/assets/a8642ec1-184f-422b-a74b-6969b4e663f2" />


**Drawing by selecting different colours from the menu bar**


<img width="1581" height="927" alt="Screenshot 2026-01-15 173050" src="https://github.com/user-attachments/assets/cf8ab06a-1f08-4420-bcfd-02da22dac100" />


**Erasing option selected**

<img width="1582" height="918" alt="Screenshot 2026-01-15 173207" src="https://github.com/user-attachments/assets/e9ae3127-808c-4fcc-b433-a59159593ebe" />

