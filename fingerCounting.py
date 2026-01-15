import cv2 as cv
import os
import time
import handTracking as htm

wCam, hCam = 640, 480

folderPath = "fingers"
myList = os.listdir(folderPath)
print(myList)
overlay = []

for impath in myList:
    image = cv.imread(f'{folderPath}/{impath}')
    overlay.append(image)

cap = cv.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

detector = htm.HandTracker(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]

while True:
    hands, img = detector.get_frame()
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        fingers = []

        # Detect hand orientation (palm facing camera or back)
        if lmList[0][0] < lmList[9][0]:
            hand_facing = 'palm'
        else:
            hand_facing = 'back'

        # Thumb detection
        if hand_facing == 'palm':
            if lmList[tipIds[0]][0] > lmList[tipIds[0] - 1][0]:
                fingers.append(1)
            else:
                fingers.append(0)
        else:
            if lmList[tipIds[0]][0] < lmList[tipIds[0] - 1][0]:
                fingers.append(1)
            else:
                fingers.append(0)

        # Other fingers - 4 fingers
        for id in range(1, 5):
            # Check if tip is above joint (for fingers pointing up)
            if lmList[tipIds[id]][1] < lmList[tipIds[id] - 2][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        totalFingers = fingers.count(1)
        print(f"Fingers up: {totalFingers}")

        """#visualize for debugging
        for id, lm in enumerate(lmList):
            cx, cy = int(lm[0]), int(lm[1])
            cv.circle(img, (cx, cy), 5, (255, 0, 255), cv.FILLED)"""

        #Overlay image
        h, w, c = overlay[totalFingers-1].shape
        img[0:h, 0:w] = overlay[totalFingers-1]

        cv.rectangle(img,(0,255),(200,425),(0,0,255),cv.FILLED)
        cv.putText(img,str(totalFingers),(45,375),cv.FONT_HERSHEY_PLAIN,10,(255,0,0),25)

    # FPS calculation
    cTime = time.time()
    fps = 1 / (cTime - pTime) if cTime != pTime else 0
    pTime = cTime
    cv.putText(img, f'FPS:{int(fps)}', (400, 70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv.imshow("Images", img)
    key = cv.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        break