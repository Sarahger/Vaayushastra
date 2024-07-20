import cv2 as cv
import numpy as np

vidCap= cv.VideoCapture(0)
prevCircle= None
dist = lambda x1,y1,x2,y2: (x1-x2)**2*(y1-y2)**2


while True:
    ret,frame = vidCap.read()
    if not ret: 
        print("Couldn't capture the video\n")
        break

    gray=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blur= cv.GaussianBlur(gray, (17,17) , 0)

    circles = cv.HoughCircles(blur, cv.HOUGH_GRADIENT, 1.2, 100, param1=30, param2=80, minRadius=15, maxRadius=200 )

    if circles is not None:
        circles=np.uint16(np.around(circles))
        chosen= None
        for i in circles[0,:]:
            if chosen is None: chosen = i
            if prevCircle is not None:
                if dist(chosen[0],chosen[1],prevCircle[0],prevCircle[1]) * dist(i[0],i[1],prevCircle[0],prevCircle[1]):
                    chosen=i

        cv.circle(frame, (chosen[0],chosen[1]), 1, (0,100,100), 3)
        cv.circle(frame, (chosen[0],chosen[1]), chosen[2], (255,0,255), 3)
        prevCircle = chosen

    cv.imshow("circles",frame)

    if cv.waitKey(1)== 27: 
        break

vidCap.release()
cv.destroyAllWindows()