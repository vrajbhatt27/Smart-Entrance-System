import json
import time
import cv2
from pyzbar.pyzbar import decode
import pyttsx3
import servo

engine = pyttsx3.init()
engine.setProperty("rate", 115)

jsonData = {}
with open('data.json') as f:
    jsonData = json.load(f)

jsonData = list(jsonData.keys())


def scan(frame):
    decoded = decode(frame)
    data = ""
    for obj in decoded:
        data = obj.data.decode()

    if data != "":
        if data in jsonData:
            engine.say("You are allowed. The door will open.")
            engine.runAndWait()
            servo.unlock()
            time.sleep(1)
            engine.say("The Door will now close")
            engine.runAndWait()
            servo.lock()
        else:
            print(data)
            engine.say("You are not allowed. Please go to control room to register yourself.")
            engine.runAndWait()

        time.sleep(0.5)
        print("Scan Complete...")


def capture():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        try:
            scan(frame)
        except:
            print("Error in Scanning...")

        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break

    cam.release()
    cv2.destroyAllWindows()


try:
    capture()
except:
    print("Error in capturing...")
    print()