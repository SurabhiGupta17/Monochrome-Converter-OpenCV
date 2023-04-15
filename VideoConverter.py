#%Convert video to grayscale and save it
import cv2

path3 = input("Enter the path of the video to be converted : (For example : C:/Users/surab/Downloads/IMG_0251.MOV) ")
cap = cv2.VideoCapture(path3)

#%Or capture video from webcam and save it to your computer
#%cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) 

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", gray)
        output.write(frame)
        #%Press 'q' to stop video from playing
        if cv2.waitKey(1) == ord("q"):
            break

cap.release()
output.release()
cv2.destroyAllWindows()
