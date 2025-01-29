import cv2
import dlib

capture = cv2.VideoCapture(0)

frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_heght = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

detector = dlib.get_frontal_face_detector()

while True:
    _, img = capture.read()
    face_bboxes = detector(img)

    print(f"{len(face_bboxes)}: face(s) detected!")

    cv2.imshow("Camera", img)
    cv2.waitKey(1)