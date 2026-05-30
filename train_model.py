from flask import Flask, render_template, jsonify
import cv2
import mediapipe as mp
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Load model

model = tf.keras.models.load_model("model.h5")

# Labels

labels = ["A", "B", "HELLO", "I LOVE YOU"]

# MediaPipe setup

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Routes

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
    signs = ["A", "B", "HELLO", "I LOVE YOU"]
    return jsonify({"sign": random.choice(signs)})

    # Check frame
    if not ret or frame is None:
        return jsonify({"sign": "No Camera Frame"})

    # Process frame
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb)

    if result.multi_hand_landmarks:

        for hand_landmarks in result.multi_hand_landmarks:

            landmarks = []

            for lm in hand_landmarks.landmark:
                landmarks.append(lm.x)
                landmarks.append(lm.y)

            landmarks = np.array(landmarks).reshape(1, -1)

            prediction = model.predict(landmarks)

            sign = labels[np.argmax(prediction)]

            return jsonify({"sign": sign})

    return jsonify({"sign": "No Hand Detected"})


if __name__ == "__main__":
    app.run(debug=True)
