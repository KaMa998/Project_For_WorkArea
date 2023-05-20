import cv2
import json
import time

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('C:\\Users\\Komol\\Desktop\\Python Project\\Project_For_WorkArea\\trainer/trainer.yml')
cascadePath = "C:\\Users\\Komol\\Desktop\\Python Project\\Project_For_WorkArea\\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX
id_to_name = ['', "Muhammad", "Buvim", "Farog'at"] # Lug'at yaratish
id_to_last_seen = {} # Lug'at yaratish

cam = cv2.VideoCapture(1)
cam.set(3, 800)
cam.set(4, 640)

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
def helo():
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
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, accuracy = recognizer.predict(gray[y:y+h,x:x+w])

        if accuracy < 100:
            id = id_to_name[id]
            accuracy = "  {0}%".format(round(100 - accuracy))
            # har bir ID uchun lug'atga nom va sanani qo'shamiz
            if id not in id_to_last_seen:
                id_to_last_seen[id] = time.time()
                print(f"{id} joyiga o'tirdi va u ishlayabdi")
                
            else:
                last_seen = id_to_last_seen[id]
                time_since_seen = time.time() - last_seen
                if time_since_seen > 43200: # 12 soat = 43200 sekund
                    id_to_last_seen[id] = time.time()
                    import pyttsx3
                    engine = pyttsx3.init()
                    engine.say(f'{id}ning vaqti tugadi')
                    
                    
                    engine.runAndWait()
                            
                        
                                 
                    
                    

        else:
            id = "Tanimadim"
            accuracy = "  {0}%".format(round(100 - accuracy))
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1) 

    cv2.imshow('camera', img)
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

helo()
cam.release()
cv2.destroyAllWindows()


