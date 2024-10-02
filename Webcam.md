Import the OpenCV library (cv2) to access its video capturing and image processing functionalities.
Initialize Webcam:

Use cv2.VideoCapture(0) to access the default webcam on your system. The argument 0 refers to the default webcam. If you have multiple webcams, you can use other numbers (1, 2, etc.) to access different cameras.
Check if Webcam Opened Successfully:

Before proceeding, verify if the webcam was successfully opened by checking the return value of cv2.VideoCapture(). If it fails, handle the error gracefully.
Start Loop to Read Frames:

Start an infinite loop to continuously capture frames from the webcam. In each iteration of the loop:
Capture a frame using cap.read(). The read() method returns two values: a boolean (ret) indicating success or failure and the actual frame (frame).
Display the Frame:

Use cv2.imshow() to display the captured frame in a window.
Exit on Key Press:

Inside the loop, use cv2.waitKey(1) to check for a key press event. If the user presses the 'q' key (or any specified key), exit the loop and stop the webcam stream.
Release the Webcam and Close Windows:

Once the loop exits, release the webcam using cap.release() and close all OpenCV windows with cv2.destroyAllWindows().
