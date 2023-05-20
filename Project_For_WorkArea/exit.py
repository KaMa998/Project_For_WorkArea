import cv2
import json
import time
from datetime import datetime


hozir = datetime.now()
soat = hozir.hour
minute = hozir.minute



recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('C:\\Users\\Komol\\Desktop\\Python Project\\Project_For_WorkArea\\trainer/trainer.yml')
cascadePath = "C:\\Users\\Komol\\Desktop\\Python Project\\Project_For_WorkArea\\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX
id_to_name = {'': '', '1': 'Muhammad'}  # Shaxslar ro'yxati
id_to_last_seen = {'1': 0}  # Oxirgi ko'rish vaqtlari lug'ati
id = 10
cam = cv2.VideoCapture(1)
cam.set(3, 800)
cam.set(4, 640)

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH))
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        id, accuracy = recognizer.predict(gray[y:y+h, x:x+w])

        if accuracy < 100:
            id = id_to_name[str(id)]
            accuracy = "  {0}%".format(round(100 - accuracy))
            
            if id not in id_to_last_seen:
                id_to_last_seen[id] = time.time()
                with open("C:\\Users\\Komol\\Desktop\\Python Project\\Project_For_WorkArea\\exit_log.txt", "a") as file:
                                file.write(f"{id}: {soat}:{minute}da ishdan ketdi\n")

        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255, 255, 255), 2)



    cv2.imshow('camera', img)
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break


cam.release()
cv2.destroyAllWindows()