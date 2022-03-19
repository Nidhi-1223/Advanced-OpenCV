# import cv2
# import mediapipe as mp
# import time

# class handDetector():
#     def __init__(self, static_image_mode= False, max_num_hands= 2, min_detection_confidence= 0.5, min_tracking_confidence= 0.5):
#         self.static_image_mode = static_image_mode 
#         self.max_num_hands = max_num_hands
#         self.min_detection_confidence = min_detection_confidence
#         self.min_tracking_confidence = min_tracking_confidence  
#         self.mpHands = mp.solutions.hands
#         self.hands = self.mpHands.Hands(
#             self.static_image_mode, 
#             self.min_tracking_confidence, 
#             self.min_detection_confidence, 
#             self.max_num_hands
#         )
#         self.mpDraw = mp.solutions.drawing_utils

#     def findHands(self,img, draw= True):
#         results = self.hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#         if results.multi_hand_landmarks != None:
#                 for handLms in results.multi_hand_landmarks:
#                     if draw:
#                         self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
#                 #     for id, lm in enumerate(handLms.landmark):
#                 #         # print(id, lm)
#                 #         h, w, c = img.shape
#                 #         cx, cy = int(lm.x * w), int(lm.y * w)
#                 #         print(id, cx, cy)
#                 #         if id == 0:
#                 #             cv2.circle(img, (cx,cy), 5, (225,8,225), cv2.FILLED)
#         return img

# def main():
#     cap = cv2.VideoCapture(0)
#     previousTime = 0
#     currentTime = 0
#     detector = handDetector()
#     while True:
#         success, img = cap.read()
#         img = cv2.flip(img, 1)

#         img = detector.findHands(img)

#         currentTime = time.time()
#         fps = 1/(currentTime - previousTime)
#         previousTime = currentTime

#         cv2.putText(img, str(int(fps)), (50,50), cv2.FONT_HERSHEY_PLAIN,3, (225,0,225),3, cv2.LINE_AA)

#         cv2.imshow("Image", img)
#         key = cv2.waitKey(20)
#         if (key == ord('q')):
#             break
#         cap.release() 
#         cv2.destroyAllWindows()
    
    
# if __name__ == "__main__":
#     main()

import cv2
import mediapipe as mp
import time
class handDetector():
    def __init__(self, static_image_mode = False, max_num_hands = 2, min_detection_confidence = 0.5, min_tracking_confidence = 0.5):
        self.static_image_mode = static_image_mode
        self.max_num_hands = max_num_hands
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        self.mpHands = mp.solutions.hands
        print(self.static_image_mode)
        self.hands = self.mpHands.Hands(self.static_image_mode, self.max_num_hands, self.min_detection_confidence, self.min_tracking_confidence)
        self.mpDraw = mp.solutions.drawing_utils
        
    def findHands(self,img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo = 0, draw = True):

        lmlist = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 3, (255, 0, 255), cv2.FILLED)
        return lmlist

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmlist = detector.findPosition(img)
        if len(lmlist) != 0:
            print(lmlist[4])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("Image", img)
        key = cv2.waitKey(20)
        if (key == ord('q')):
            break
        cap.release() 
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()