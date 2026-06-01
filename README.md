Sign Language Interpreter Using Robotics Hand
📌 Project Overview

The Sign Language Interpreter Using Robotics Hand is a real-time system that recognizes sign language gestures using Computer Vision and Machine Learning and translates them into meaningful text. The recognized gestures are then replicated by a robotic hand, enabling effective communication between sign language users and non-sign language users.

This project combines Artificial Intelligence, Computer Vision, and Robotics to create an interactive and accessible communication solution.

🎯 Features
Real-time sign language recognition using a webcam
Hand landmark detection using MediaPipe
Gesture classification using a trained TensorFlow/Keras model
User-friendly web interface built with Flask
Automatic prediction display
Robotic hand gesture replication
Support for multiple sign language gestures
Easy-to-use dashboard and practice mode

🛠️ Technologies Used
Python
TensorFlow / Keras
OpenCV
MediaPipe
Flask
NumPy
HTML
CSS
JavaScript
Arduino (for robotic hand control)

)
📂 Project Structure
project/
│
├── app.py
├── train_model.py
├── model.h5
├── templates/
│   ├── practice.html
│   └── robot.html
├── dataset/
├── README.md
└── requirements.txt

⚙️ Installation
1. Clone the Repository
git clone https://github.com/your-username/Sign-language-interpreter-using-robotics-hand.git
2. Move to Project Directory
cd Sign-language-interpreter-using-robotics-hand
3. Install Dependencies
pip install -r requirements.txt
4. Run the Application
python app.py
5. Open Browser
http://127.0.0.1:5000

🧠 Working
Webcam captures hand gestures.
MediaPipe extracts hand landmarks.
The trained TensorFlow model predicts the sign.
The prediction is displayed on the web interface.
Corresponding commands can be sent to the robotic hand.
The robotic hand reproduces the recognized gesture.
