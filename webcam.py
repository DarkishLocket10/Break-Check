import time
import cv2
from win10toast import ToastNotifier

# Initialize toaster
toaster = ToastNotifier()

# Initialize the camera
camera = cv2.VideoCapture(0)

# Initialize the timer
start_time = time.time()

# Initialize the flag that indicates if the message was displayed
message_displayed = False

# Continuously capture frames from the camera
while True:
    # Capture frame-by-frame
    ret, frame = camera.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = cv2.CascadeClassifier(
        "haarcascade_frontalface_default.xml").detectMultiScale(gray, 1.3, 5)

    # Check if a face was detected
    if len(faces) > 0:
        # Calculate the elapsed time
        elapsed_time = time.time() - start_time

        # Check if the face has been detected for more than 6 seconds
        if elapsed_time > 6:
            # Display a message
            cv2.putText(frame, "You have been sitting for too long!",
                        (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            message_displayed = True
            toaster.show_toast("Alert", "You have been sitting for too long!")
    else:
        # Calculate the elapsed time
        elapsed_time = time.time() - start_time

        # Check if the face has been obscured for more than 4 seconds
        if elapsed_time > 4:
            # Reset the timer
            start_time = time.time()
            message_displayed = False

    # Check if the message should be displayed
    if message_displayed:
        # Calculate the elapsed time
        elapsed_time = time.time() - start_time

        # Check if the user has been gone for more than 15 seconds
        if elapsed_time > 15:
            # Reset the flag
            message_displayed = False
    else:
        # Show the frame
        cv2.imshow("Camera", frame)

    # Check if the user pressed the "ESC" key
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break