import face_recognition
import cv2
import pickle
import os

def login_user(logger):
    if not os.path.exists("encodings.pkl"):
        print("[ERROR] No registered users found.")
        return

    known_encodings = []
    known_names = []
    
    with open("encodings.pkl", "rb") as f:
        while True:
            try:
                name, encoding = pickle.load(f)
                known_encodings.append(encoding)
                known_names.append(name)
            except EOFError:
                break

    cap = cv2.VideoCapture(0)
    print("[INFO] Capturing for login...")
    ret, frame = cap.read()
    cap.release()
    cv2.destroyAllWindows()

    if not ret:
        print("[ERROR] Failed to capture frame.")
        return

    encodings = face_recognition.face_encodings(frame)
    if not encodings:
        print("[ERROR] No face found.")
        return

    match = face_recognition.compare_faces(known_encodings, encodings[0])
    if True in match:
        matched_idx = match.index(True)
        name = known_names[matched_idx]
        print(f"[SUCCESS] Logged in as {name}")
        logger.log_action(name, "Logged In")
    else:
        print("[ERROR] Face not recognized.")
