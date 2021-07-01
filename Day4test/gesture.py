import cv2
import mediapipe as mp
import numpy as np

# import matplotlib.pyplot as plt


def p_l_dist(pl1,pl2,p): 
    d = np.linalg.norm(np.cross(p-pl1, p-pl2))/np.linalg.norm(pl1-pl2)
    return d

def pl517(p):
    return p_l_dist(fp5,fp17,p)

def pl05(p):
    return p_l_dist(fp0,fp5,p)

def side_of_point(pl1,pl2,p1,p2):
    det1 = np.linalg.det(np.vstack((np.array([pl1,pl2,p1]).T,np.array([1,1,1]))))
    det2 = np.linalg.det(np.vstack((np.array([pl1,pl2,p2]).T,np.array([1,1,1]))))
    return int(det1*det2/np.abs(det1*det2))


def sp517(p1,p2):
    return side_of_point(fp5,fp17,p1,p2)
    
def sp05(p1,p2):
    return side_of_point(fp5,fp0,p1,p2)

def gest_rec():
    print(sp517(fp8,fp6),sp517(fp12,fp10),sp517(fp16,fp14),sp517(fp20,fp18),sp05(fp4,fp17))
    delta = [sp517(fp8,fp6),sp517(fp12,fp10),sp517(fp16,fp14),sp517(fp20,fp18),sp05(fp4,fp17)]
    print(pl517(fp8)-pl517(fp6),pl517(fp12)-pl517(fp10),pl517(fp16)-pl517(fp14),pl517(fp20)-pl517(fp18))
    if pl517(fp8)-pl517(fp6)<0:
        return "3"
    elif delta == [1,1,1,1,1]:
        return "4"
    elif delta == [1,1,1,1,-1]:
        return "5"
    elif delta == [1, 1, -1, -1, 0] or delta == [1, 1, -1, -1, 1]:
        return "2"
    elif delta == [1,-1,-1,-1,0] or delta == [1, -1, -1, -1, 1]:
        return "1"
    else:
        return "0"

def img_rec(IMAGE_FILES):
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    with mp_hands.Hands(
            static_image_mode=True,
            max_num_hands=2,
            min_detection_confidence=0.5) as hands:
          for idx, file in enumerate(IMAGE_FILES):
            # Read an image, flip it around y-axis for correct handedness output (see
            # above).
            image = cv2.flip(cv2.imread(file), 1)
            # Convert the BGR image to RGB before processing.
            results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

            # Print handedness and draw hand landmarks on the image.
    #         print('Handedness:', results.multi_handedness)
            if not results.multi_hand_landmarks:
                continue
            image_height, image_width, _ = image.shape
            annotated_image = image.copy()
            for hand_landmarks in results.multi_hand_landmarks:
    #             print('hand_landmarks:', hand_landmarks)
    #             print(
    #               f'Index finger tip coordinates: (',
    #               f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
    #               f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height})'
    #           )

                global fp0,fp4,fp5,fp6,fp8,fp10,fp12,fp14,fp16,fp17,fp18,fp20
                fp5 = np.array((hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x, hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y))
                fp17 = np.array((hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].x, hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y))
                fp0 = np.array((hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x, hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y))

                fp4 = np.array((hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x, hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y))
                fp8 = np.array((hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x, hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y))
                fp6 = np.array((hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].x, hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y))
                fp12 = np.array((hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x, hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y))
                fp10 = np.array((hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].x, hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y))
                fp16 = np.array((hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x, hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y))
                fp14 = np.array((hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].x, hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y))
                fp20 = np.array((hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x, hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y))
                fp18 = np.array((hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].x, hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y))
                return gest_rec()
    #             mp_drawing.draw_landmarks(
    #             annotated_image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    #         cv2.imwrite(
    #             './tmp/annotated_image' + str(idx) + '.png', cv2.flip(annotated_image, 1))
    #         plt.imshow(cv2.flip(annotated_image, 1))
    #         plt.show()
