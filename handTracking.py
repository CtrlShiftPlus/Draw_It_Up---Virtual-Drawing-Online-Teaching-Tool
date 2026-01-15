# handTracking.py
import cv2
from cvzone.HandTrackingModule import HandDetector

class HandTracker:
    def __init__(self, detectionCon=0.8, maxHands=2):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 1200)
        self.cap.set(4, 720)
        self.detector = HandDetector(detectionCon=detectionCon, maxHands=maxHands)

        self.tipIds = [4, 8, 12, 16, 20]

    def get_frame(self):
        success, img = self.cap.read()
        if not success:
            return None, None
        
        
        # Detect hands once here
        self.hands, img = self.detector.findHands(img)
        return self.hands, img

    def findPosition(self, img, handNo=0, draw=True):
        """Find landmarks of hands, using previously detected hands"""
        self.lmList=[]
        if self.hands is None or len(self.hands) == 0:
            return []

        if len(self.hands) > handNo:
            hand = self.hands[handNo]
            self.lmList = hand['lmList']
            return self.lmList
        return []

    def fingersUp(self):
        fingers = []

        # Detect hand orientation (palm facing camera or back)
        if self.lmList[0][0] < self.lmList[9][0]:
            hand_facing = 'palm'
        else:
            hand_facing = 'back'

        # Thumb detection
        if hand_facing == 'palm':
            if self.lmList[self.tipIds[0]][0] > self.lmList[self.tipIds[0] - 1][0]:
                fingers.append(1)
            else:
                fingers.append(0)
        else:
            if self.lmList[self.tipIds[0]][0] < self.lmList[self.tipIds[0] - 1][0]:
                fingers.append(1)
            else:
                fingers.append(0)

        # Other fingers - 4 fingers
        for id in range(1, 5):
            # Check if tip is above joint (for fingers pointing up)
            if self.lmList[self.tipIds[id]][1] < self.lmList[self.tipIds[id] - 2][1]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()
