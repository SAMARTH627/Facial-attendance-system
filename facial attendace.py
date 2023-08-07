import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime



vide0_capture = cv2.VideoCapture(0)

#LOADING IMAGES OF STUDENTS

sam_img = face_recognition.load_image_file("images/SAM.jpg")
sam_encoding = face_recognition.face_encoding(sam_img)[0]
kunal_img = face_recognition.load_image_file("images/KUNAL.jpg")
kunal_encoding = face_recognition.face_encoding(kunal_img)[0]

known_faces_encodings = [sam_encoding, kunal_encoding]
known_faces_names = ["Sam","Kunal"]

#studes who will come
students = known_faces_names.copy()
face_locations = []
face_encoding = []



#time of entering

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)


while True:
    _, frame = vide0_capture.read()
    small_frame = cv2.resize(frame, (0,0), fx = 0.25, fy = 0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    #recognize faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)


    for face_encoding in face_encodings:
        mathes = face_recognition.compare_faces(known_faces_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_faces_encodings,face_encoding)
        best_match_index = np.argm(face_distance)
        if(mathes[best_match_index]):
            name = known_faces_names[best_match_index]


#if present

        if name in known_faces_names:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (0,100)
            fontScale = 1.5
            fontColor = (255, 0, 0)
            thickness = 3
            lineType = 2
            cv2.putText(frame, name + "Present", bottomLeftCornerOfText, fontScale,  fontColor, thickness, lineType    )



        if name in students:
            students.remove(name)
            current_time = now.strftime("%H-%M-%S")
            lnwriter.writerow([name, current_time])

    cv2.imshow("Attendace", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.VideoCapture.release()
cv2.destroyAllWindows()
f.close()




