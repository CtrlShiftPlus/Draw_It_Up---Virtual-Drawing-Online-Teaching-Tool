import numpy as np
import os
import cv2 as cv
import handTracking as htm

brushThickness=15
eraseThickness=50

folderPath = "pictures"
myList = os.listdir(folderPath)
#print(myList)
overlay = []

for impath in myList:
    image = cv.imread(f'{folderPath}/{impath}')
    if image is not None:
        overlay.append(image)

#print(len(overlay))

header = overlay[0]
drawColour=(0,0,255)

detector = htm.HandTracker(detectionCon=0.85)
xp,yp=0,0
imgCanvas=np.zeros((720,1280,3),np.uint8)
imgCanvas=cv.flip(imgCanvas,1)

while True:
    hands, img = detector.get_frame()

    
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        
        x1, y1 = lmList[8][0], lmList[8][1]
        x2, y2 = lmList[12][0], lmList[12][1]

        fingers=detector.fingersUp()
        

        #Selection mode - 2 fingers up
        if (fingers[1] and fingers[2]) and (fingers[3]==False):
            xp,yp=0,0
            #print("Selection Mode")

            #checking from the click and changing the menu
            if y1<125:
                if 250<x1<450:
                    header=overlay[0]
                    drawColour=(0,0,255)
                elif 500<x1<650:
                    header=overlay[1]
                    drawColour=(0,255,255)
                elif 700<x1<950:
                    header=overlay[2]
                    drawColour=(0,255,0)
                elif 1050<x1<1200:
                    header=overlay[3]
                    drawColour=(0,0,0)
                
            cv.rectangle(img,(x1,y1-25),(x2,y2+25),drawColour,cv.FILLED)

        #Drawing Mode - index finger up
        if fingers[1] and fingers[2]==False:
            cv.circle(img,(x1,y1),15,drawColour,cv.FILLED)
            #print("Drawing Mode")
            if xp==0 and yp==0:
                xp,yp=x1,y1

            if drawColour==(0,0,0):
                cv.line(img,(xp,yp),(x1,y1),drawColour,eraseThickness)
                cv.line(imgCanvas,(xp,yp),(x1,y1),drawColour,eraseThickness)
            else:
                cv.line(img,(xp,yp),(x1,y1),drawColour,brushThickness)
                cv.line(imgCanvas,(xp,yp),(x1,y1),drawColour,brushThickness)
            

            #Reseting points to previous coordinates
            xp,yp=x1,y1


    imgGray=cv.cvtColor(imgCanvas,cv.COLOR_BGR2GRAY)
    _, imgInv=cv.threshold(imgGray,50,255,cv.THRESH_BINARY_INV)
    imgInv=cv.cvtColor(imgInv,cv.COLOR_GRAY2BGR)
    img=cv.bitwise_and(img,imgInv)
    img=cv.bitwise_or(img,imgCanvas)

    # First image on top
    h, w, c = header.shape
    img[0:h, 0:w] = header
    img = cv.addWeighted(img, 1, imgCanvas, 0.5,0)

    cv.imshow("Image", img)
    #cv.imshow("Canvas",imgCanvas)

    key = cv.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        detector.release()
        break
