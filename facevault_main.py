import os
import sys
import face_register
import face_login
import emotion_detector
from logger import Logger
from utils import menu_ui

if __name__ == "__main__":
    logger = Logger()
    while True:
        choice = menu_ui()

        if choice == '1':
            face_register.register_user(logger)

        elif choice == '2':
            face_login.login_user(logger)

        elif choice == '3':
            emotion_detector.detect_emotion()

        elif choice == '4':
            print("[INFO] Exiting FaceVault. Goodbye!")
            sys.exit()

        else:
            print("[ERROR] Invalid choice. Please try again.")
            
