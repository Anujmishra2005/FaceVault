import cv2
from deepface import DeepFace

def detect_emotion():
    cap = cv2.VideoCapture(0)
    print("[INFO] Detecting emotion. Look at the camera.")
    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("[ERROR] Could not access camera.")
        return

    result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
    emotion = result[0]['dominant_emotion']
    print(f"[RESULT] Detected Emotion: {emotion}")
