import face_recognition
import cv2
import json
import os
import pickle

def register_user(logger):
    name = input("Enter your name: ")
    cap = cv2.VideoCapture(0)

    print("[INFO] Capturing image. Please look at the camera...")
    ret, frame = cap.read()
    cap.release()
    cv2.destroyAllWindows()

    if not ret:
        print("[ERROR] Failed to capture image.")
        return

    face_encodings = face_recognition.face_encodings(frame)
    if not face_encodings:
        print("[ERROR] No face detected. Try again.")
        return

    with open("encodings.pkl", "ab") as f:
        pickle.dump((name, face_encodings[0]), f)

    users = {}
    if os.path.exists("users.json"):
        with open("users.json", "r") as f:
            users = json.load(f)

    users[name] = {"registered": True}
    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)

    logger.log_action(name, "Registered")
    print(f"[SUCCESS] User '{name}' registered successfully.")
