import time
import cv2
from pyzbar.pyzbar import decode
import pyttsx3
import servo

engine = pyttsx3.init()
engine.setProperty("rate", 115)


def scan(frame):
    decoded = decode(frame)
    data = ""
    for obj in decoded:
        data = obj.data.decode()

    if data != "":
        if data == "Vraj Bhatt 18IT013":
            engine.say("You are allowed. The door will open.")
            engine.runAndWait()
            servo.unlock()
            time.sleep(0.5)
            engine.say("The Door will now close")
            engine.runAndWait()
            servo.lock()
        else:
            print(data)
            engine.say("Not Allowed")
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

        scan(frame)

        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break

    cam.release()
    cv2.destroyAllWindows()


capture()
