import cv2 as cv
import numpy as np

choice= input("Enter colour: ").lower()

if choice=='green':
    #green
    low= np.array([54,65,40])
    high= np.array([95,255,255])

elif choice=='red':
    #red
    low= np.array([167,117,87])
    high= np.array([180,255,255])

elif choice=='yellow':
    #yellow
    low= np.array([18,94,83])
    high= np.array([32,255,255])

elif choice=='violet':
    #violet
    low= np.array([129,77,56])
    high= np.array([170,255,255])

elif choice=='brown':
    #brown
    low= np.array([7,114,50])
    high= np.array([16,255,255])

elif choice=='orange':
    #orange
    low= np.array([8,170,120])
    high= np.array([20,255,255])


vidCap= cv.VideoCapture(0)
prevCircle= None
dist = lambda x1,y1,x2,y2: (x1-x2)**2*(y1-y2)**2


while True:
    ret,frame = vidCap.read()
    if not ret: 
        print("Couldn't capture the video\n")
        break

    # Convert the frame to the HSV color space
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Create a mask using the inRange function
    mask = cv.inRange(hsv, low, high)

    # Blur using 3 * 3 kernel.
    mask_blurred = cv.GaussianBlur(mask, (9, 9), 2)

    circles = cv.HoughCircles(mask_blurred, cv.HOUGH_GRADIENT, 1.2, 100, param1=20, param2=80, minRadius=5, maxRadius=300 )

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