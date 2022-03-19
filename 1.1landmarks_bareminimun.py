# reference = https://techtutorialsx.com/2021/04/20/python-real-time-hand-tracking/#Real-time_hand_tracking_and_landmark_estimation
#**************************************************method 1**********************************************************
# import cv2
# from cv2 import cvtColor
# cv2.__version__
# import mediapipe as mp
# import time

# cap = cv2.VideoCapture(0)
# mpHands = mp.solutions.hands
# mpDraw = mp.solutions.drawing_utils

# with mpHands.Hands(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=2) as hands:
#     while(True):
#         success, img = cap.read()
#         img = cv2.flip(img, 1)
        
#         results = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#         print(results.multi_hand_landmarks)         #to see if the programme detects the hand or not

#         if results.multi_hand_landmarks != None:
#             for handLms in results.multi_hand_landmarks:
#                 mpDraw.draw_landmarks(img, handLms,mpHands.HAND_CONNECTIONS)
                    
        

#         cv2.imshow("Image", img)
#         key = cv2.waitKey(20)
#         if (key == ord('q')):
#             break

# cv2.destroyAllWindows()
# cap.release()

#****************************************************************method 2*********************************************
import cv2
import mediapipe as mp
import time

#creating a video object
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False, 
    min_detection_confidence=0.5, 
    min_tracking_confidence=0.5, 
    max_num_hands=2
)
mpDraw = mp.solutions.drawing_utils


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    # imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks != None:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Image", img)
    key = cv2.waitKey(20)
    if (key == ord('q')):
        break

cv2.destroyAllWindows()
cap.release()  