import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

# LOADING IMAGES OF STUDENTS

sam_img = face_recognition.load_image_file("images\SAM.jpeg")
sam_encoding = face_recognition.face_encodings(sam_img)[0]
kunal_img = face_recognition.load_image_file("images\KUNAL.jpeg")
kunal_encoding = face_recognition.face_encodings(kunal_img)[0]

known_faces_encodings = [sam_encoding, kunal_encoding]
known_faces_names = ["Sam", "Kunal"]

# Students who will come
students = known_faces_names.copy()

# Create a CSV file for attendance
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
csv_filename = f"{current_date}.csv"
f = open(csv_filename, "w+", newline="")
csv_writer = csv.writer(f)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Recognize faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_faces_encodings, face_encoding)
        face_distances = face_recognition.face_distance(known_faces_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            name = known_faces_names[best_match_index]

            # If present
            if name in students:
                students.remove(name)
                current_time = now.strftime("%H-%M-%S")
                csv_writer.writerow([name, current_time])

            # Draw a rectangle and label on the face
            top, right, bottom, left = face_locations[best_match_index]
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, name + " Present", (left, bottom + 30), font, 1.0, (0, 255, 0), 1)

    cv2.imshow("Attendance",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()
