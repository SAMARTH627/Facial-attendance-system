
The provided Python script appears to be a simple facial recognition attendance system using the face_recognition and cv2 (OpenCV) libraries. Here's a description that you can use for a GitHub repository:

Facial Recognition Attendance System
Overview
This project is a simple facial recognition attendance system implemented in Python using the popular libraries face_recognition and OpenCV. The system captures video frames from a webcam, recognizes faces of pre-loaded students, and maintains attendance records in a CSV file.

Features
Real-time Facial Recognition: The system continuously captures video frames from the webcam, detects faces, and matches them against a predefined set of known student faces.

Attendance Logging: When a recognized face is detected, the system records the student's name and the current timestamp in a CSV file, creating an attendance log for the day.

Dynamic Student List: The list of students expected to attend the session is initially populated with known faces. As students are recognized, their names are removed from the list.

User Interface: The system provides a simple user interface using OpenCV to display the live video feed with rectangles around recognized faces and attendance status.

*Usage*

Install Dependencies:
Install the required Python libraries

using pip install -r requirements.txt.
Prepare Student Images:

Add images of students to the "images" directory, naming them appropriately.
Run the Script:

Execute the script (attendance_system.py) to start the facial recognition attendance system.
Terminate the Program:

Press 'q' to terminate the program and close the video feed window.

View Attendance Records:
Attendance records are stored in a CSV file named with the current date (e.g., "2023-01-01.csv").
File Structure
attendance_system.py: The main Python script for the facial recognition attendance system.
images/: Directory containing images of known students.
requirements.txt: List of required Python libraries.
<current_date>.csv: CSV file storing attendance records for the current date.


OUTPUT:
![image](https://github.com/SAMARTH627/Facial-attendance-system/assets/111736287/6261177b-8108-41ff-a025-65b94b595165)

Dependencies
face_recognition: Face recognition library.
OpenCV: Computer vision library for image and video processing.
Notes
This project serves as a basic template for a facial recognition attendance system and can be extended with additional features or improvements.
# Facial-attendance-system
