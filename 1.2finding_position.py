#theres a distance between the actual point and the point detected
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

previousTime = 0
currentTime = 0


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    # imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks != None:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * w)
                print(id, cx, cy)
                if id == 0:
                    cv2.circle(img, (cx,cy), 10, (225,8,225), cv2.FILLED)


            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)


    currentTime = time.time()
    fps = 1/(currentTime - previousTime)
    previousTime = currentTime

    cv2.putText(img, str(int(fps)), (50,50), cv2.FONT_HERSHEY_PLAIN,3, (225,0,225),3, cv2.LINE_AA)

    cv2.imshow("Image", img)
    key = cv2.waitKey(20)
    if (key == ord('q')):
        break

cv2.destroyAllWindows()
cap.release() 