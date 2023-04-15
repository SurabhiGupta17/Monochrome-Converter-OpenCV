import cv2

#%taking user input
path1 = input("Enter the path of the image to be converted : (For example : C:/Users/surab/Downloads/IMG_A01.jpg) ")
path2 = input("Enter the path of the changed image : (For example : C:/Users/surab/Downloads/Gray.jpg) ")

#%conversion to grayscale
img1 = cv2.imread(path1, 0)
img1 = cv2.resize(img1, (1000, 600))
cv2.imshow("Grayscale", img1)

#%saving image
print("Press 's' to save the converted image.")
k = cv2.waitKey(0)
if k == ord("s"):
  cv2.imwrite(path2, img1)
else:
  cv2.destroyAllWindows()
