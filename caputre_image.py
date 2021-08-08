import cv2
from face_rec import classify_face


def capture():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break

        elif k % 256 == 32:
            # SPACE pressed
            img_name = "test.jpg"
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            classify_face('test.jpg')

    cam.release()
    cv2.destroyAllWindows()


capture()
