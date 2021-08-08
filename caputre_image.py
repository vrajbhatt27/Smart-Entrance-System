import cv2
from face_rec import classify_face


def capture():
    print("Here")
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0

    while True:
        print("--Here")
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
            print("Space pressed")
            img_name = "test.jpg"
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
            print(classify_face('test.jpg'))

    cam.release()
    cv2.destroyAllWindows()


capture()
