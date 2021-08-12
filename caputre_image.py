import cv2
from pyzbar.pyzbar import decode


def capture():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    while True:
        qrcode = False
        qrdata = ""
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        try:
            decodedobj = decode(frame)
            for obj in decodedobj:
                qrcode = True
                qrdata = obj.data.decode()

            if qrcode:
                print("Person Allowed")
                qrcode = False
        except:
            pass

        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break

    cam.release()
    cv2.destroyAllWindows()


capture()
