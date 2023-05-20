import cv2
import mediapipe as mp
from AppOpener import open, close
import subprocess


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

#webcam input
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue

    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    height, width, _ = image.shape
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        if hand_landmarks.landmark[4].y > hand_landmarks.landmark[3].y: #ok
          subprocess.Popen('start EVKey64:', shell=True)
        elif hand_landmarks.landmark[7].y > hand_landmarks.landmark[8].y:
          close("Messenger")
          '''
          try:
            subprocess.run(["taskkill", "/f", "/im", "Messenger.exe"], check=True)
            print("The application", "Messenger", "has been closed successfully.")
            continue
          except subprocess.CalledProcessError:
            print("The application", "Messenger", "could not be found.")
            '''
        elif hand_landmarks.landmark[11].y > hand_landmarks.landmark[12].y:
          open("Word")
        elif hand_landmarks.landmark[15].y > hand_landmarks.landmark[16].y:
          open("Excel")
        elif hand_landmarks.landmark[19].y > hand_landmarks.landmark[20].y: #ok
          open("Opera GX Browser")
        mp_drawing.draw_landmarks(
          image,
          hand_landmarks,
          mp_hands.HAND_CONNECTIONS,
          mp_drawing_styles.get_default_hand_landmarks_style(),
          mp_drawing_styles.get_default_hand_connections_style())
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break
cap.release()
        
