import cv2
# capture video from web cam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # cap is define for video 
fourcc = cv2.VideoWriter_fourcc(*"XVID") #fourcc is parameter for video, we can also use DIVX, MJPG
output = cv2.VideoWriter("D:\\output.avi", fourcc, 20.0, (640, 480)) 
print(cap)
while cap.isOpened():
    ret, frame = cap.read()
    if ret== True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        frame = cv2.flip(frame,1) #here flip is used to lip the video at recording time (0 show flip and 1 show straight)
        cv2.imshow("Gray Frame", gray) 
        cv2.imshow("Color Frame", frame) 
        output.write(gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
output.release()
cv2.destroyAllWindows()