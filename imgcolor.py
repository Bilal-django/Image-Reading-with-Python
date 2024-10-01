import cv2
# Reading the image from the file path
img = cv2.imread("D:\zaid workshop placemeant\clothes pic\men\menpro52.png")
img = cv2.resize(img,(1200,700))
print(img)
cv2.imshow("original", img)

cv2.waitKey()
cv2.destroyAllwindows()