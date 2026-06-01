from flask import Flask, render_template, jsonify, redirect
import cv2
import mediapipe as mp
import numpy as np
import tensorflow as tf
from flask import request


app = Flask(__name__)

# Load model

model = tf.keras.models.load_model("model.h5")

# Labels

labels = ["A", "B", "HELLO", "I LOVE YOU"]

# MediaPipe setup

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Routes

@app.route('/robot_control', methods=['POST'])
def robot_control():
    data = request.json
    sign = data.get("sign")

    print("Robot performing:", sign)

    return {"status": "ok"}

@app.route('/')
def home():
 return render_template("index.html")

@app.route('/robot')
def robot():
  return render_template("robot.html")

@app.route('/practice')
def practice():
  return render_template("practice.html")

import random

@app.route('/detect')
def detect():

    cap = cv2.VideoCapture(0)

    ret, frame = cap.read()

    if not ret:
        cap.release()
        return jsonify({"sign": "Camera Error"})

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb)

    cap.release()

    if result.multi_hand_landmarks:

        for hand_landmarks in result.multi_hand_landmarks:

            landmarks = []

            for lm in hand_landmarks.landmark:
                landmarks.append(lm.x)
                landmarks.append(lm.y)

            landmarks = np.array(landmarks).reshape(1, -1)

            prediction = model.predict(landmarks, verbose=0)

            sign = labels[np.argmax(prediction)]

            return jsonify({"sign": sign})

    return jsonify({"sign": "No Hand Detected"})


if __name__ == "__main__":
    app.run(debug=True)         
