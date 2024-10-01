import cv2
# Reading the image from the file path
img = cv2.imread("D:\zaid workshop placemeant\clothes pic\men\menpro52.png", 0) # 0 show black and white picture and 1 show original
img = cv2.resize(img,(1200,700)) 
print(img)
cv2.imshow("original", img)
# Wait for a key press and close the window
cv2.waitKey()
cv2.destroyAllwindows()
