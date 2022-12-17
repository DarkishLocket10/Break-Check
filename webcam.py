import time
import cv2
from win10toast import ToastNotifier
import tkinter as tk

# Initialize toaster
toaster = ToastNotifier()

def webcam():

    # Initialize the camera
    camera = cv2.VideoCapture(1)

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

            # Check if the face has been detected for more than 45 Minutes
            if elapsed_time > 2700:
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

            # Check if the user has been gone for more than 60 seconds
            if elapsed_time > 60:
                # Reset the flag
                message_displayed = False
        else:
            # Show the frame
            cv2.imshow("Camera", frame)

        # Check if the user pressed the "ESC" key
        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break

    # Relase the camera
    camera.release()
    cv2.destroyAllWindows()

def gui():
    # Import tkinter
    import tkinter as tk

    # Set the window size and position
    window_width = 300
    window_height = 200
    window_x = 50
    window_y = 50

    # Create the main window
    window = tk.Tk()
    window.title("Webcam Controller")
    window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

    # Set the font and text color for the buttons
    button_font = ("Arial", 20, "bold")
    button_fg = "white"
    button_bg = "#0072c6"

    # Define the function that will be called when the "Start System" button is clicked
    def start_system():
        # Call the webcam function here
        webcam()

    # Define the function that will be called when the "Finish" button is clicked
    def finish():
        # Kill the webcam function here
        pass

    # Create the "Start System" button
    start_button = tk.Button(text="Press to begin system", command=start_system, font=button_font, fg=button_fg, bg=button_bg)
    start_button.pack(fill=tk.BOTH, expand=1)

    # Create the "Finish" button
    finish_button = tk.Button(text="Finish", command=finish, font=button_font, fg=button_fg, bg=button_bg)
    finish_button.pack(fill=tk.BOTH, expand=1)

    # Run the main loop
    tk.mainloop()




if __name__ == "__main__":
    gui()
    