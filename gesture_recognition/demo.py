from os import stat
import cv2
import mediapipe as mp
import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
url = "http://localhost:8080/"
path = "./chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get(url)
js="var q=document.documentElement.scrollTop=10000"



def vector_2d_angle(v1, v2):
    """
    求解二维向量的角度
    """
    v1_x = v1[0]
    v1_y = v1[1]
    v2_x = v2[0]
    v2_y = v2[1]
    try:
        angle_ = math.degrees(
            math.acos(
                (v1_x * v2_x + v1_y * v2_y)
                / (((v1_x ** 2 + v1_y ** 2) ** 0.5) * ((v2_x ** 2 + v2_y ** 2) ** 0.5))
            )
        )
    except:
        angle_ = 65535.0
    if angle_ > 180.0:
        angle_ = 65535.0
    return angle_


def hand_angle(hand_):
    angle_list = []
    # ---------------------------- thumb 大拇指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0]) - int(hand_[2][0])), (int(hand_[0][1]) - int(hand_[2][1]))),
        ((int(hand_[3][0]) - int(hand_[4][0])), (int(hand_[3][1]) - int(hand_[4][1]))),
    )
    angle_list.append(angle_)
    # ---------------------------- index 食指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0]) - int(hand_[6][0])), (int(hand_[0][1]) - int(hand_[6][1]))),
        ((int(hand_[7][0]) - int(hand_[8][0])), (int(hand_[7][1]) - int(hand_[8][1]))),
    )
    angle_list.append(angle_)
    # ---------------------------- middle 中指角度
    angle_ = vector_2d_angle(
        (
            (int(hand_[0][0]) - int(hand_[10][0])),
            (int(hand_[0][1]) - int(hand_[10][1])),
        ),
        (
            (int(hand_[11][0]) - int(hand_[12][0])),
            (int(hand_[11][1]) - int(hand_[12][1])),
        ),
    )
    angle_list.append(angle_)
    # ---------------------------- ring 无名指角度
    angle_ = vector_2d_angle(
        (
            (int(hand_[0][0]) - int(hand_[14][0])),
            (int(hand_[0][1]) - int(hand_[14][1])),
        ),
        (
            (int(hand_[15][0]) - int(hand_[16][0])),
            (int(hand_[15][1]) - int(hand_[16][1])),
        ),
    )
    angle_list.append(angle_)
    # ---------------------------- pink 小拇指角度
    angle_ = vector_2d_angle(
        (
            (int(hand_[0][0]) - int(hand_[18][0])),
            (int(hand_[0][1]) - int(hand_[18][1])),
        ),
        (
            (int(hand_[19][0]) - int(hand_[20][0])),
            (int(hand_[19][1]) - int(hand_[20][1])),
        ),
    )
    angle_list.append(angle_)
    return angle_list


def h_gesture(angle_list):
    thr_angle = 65.0
    thr_angle_thumb = 53.0
    thr_angle_s = 49.0
    gesture_str = None
    if 65535.0 not in angle_list:
        if (
            (angle_list[0] > thr_angle_thumb)
            and (angle_list[1] > thr_angle)
            and (angle_list[2] > thr_angle)
            and (angle_list[3] > thr_angle)
            and (angle_list[4] > thr_angle)
        ):
            gesture_str = "Fist"
        elif (
            (angle_list[0] < thr_angle_s)
            and (angle_list[1] < thr_angle_s)
            and (angle_list[2] < thr_angle_s)
            and (angle_list[3] < thr_angle_s)
            and (angle_list[4] < thr_angle_s)
        ):
            gesture_str = "Five"
        elif (
            (angle_list[0] < thr_angle_s)
            and (angle_list[1] < thr_angle_s)
            and (angle_list[2] > thr_angle)
            and (angle_list[3] > thr_angle)
            and (angle_list[4] > thr_angle)
        ):
            gesture_str = "Pistol"
        elif (
            (angle_list[0] < thr_angle_s)
            and (angle_list[1] < thr_angle_s)
            and (angle_list[2] > thr_angle)
            and (angle_list[3] > thr_angle)
            and (angle_list[4] < thr_angle_s)
        ):
            gesture_str = "Love"
        elif (
            (angle_list[0] > 5)
            and (angle_list[1] < thr_angle_s)
            and (angle_list[2] > thr_angle)
            and (angle_list[3] > thr_angle)
            and (angle_list[4] > thr_angle)
        ):
            gesture_str = "One"
        elif (
            (angle_list[0] < thr_angle_s)
            and (angle_list[1] > thr_angle)
            and (angle_list[2] > thr_angle)
            and (angle_list[3] > thr_angle)
            and (angle_list[4] < thr_angle_s)
        ):
            gesture_str = "Six"
        elif (
            (angle_list[0] > thr_angle_thumb)
            and (angle_list[1] < thr_angle_s)
            and (angle_list[2] < thr_angle_s)
            and (angle_list[3] < thr_angle_s)
            and (angle_list[4] > thr_angle)
        ):
            gesture_str = "Three"
        elif (
            (angle_list[0] < thr_angle_s)
            and (angle_list[1] > thr_angle)
            and (angle_list[2] > thr_angle)
            and (angle_list[3] > thr_angle)
            and (angle_list[4] > thr_angle)
        ):
            gesture_str = "Group 8, nice job."
        elif (
            (angle_list[0] > thr_angle_thumb)
            and (angle_list[1] < thr_angle_s)
            and (angle_list[2] < thr_angle_s)
            and (angle_list[3] > thr_angle)
            and (angle_list[4] > thr_angle)
        ):
            gesture_str = "Two"
    # if gesture_str == "five":
        
    #     driver.fullscreen_window()
    return gesture_str


def detect():
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.75,
        min_tracking_confidence=0.75,
    )
    cap = cv2.VideoCapture(0)
    while True:
        status = []
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)
        results = hands.process(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
                )
                hand_local = []
                for i in range(21):
                    x = hand_landmarks.landmark[i].x * frame.shape[1]
                    y = hand_landmarks.landmark[i].y * frame.shape[0]
                    hand_local.append((x, y))
                if hand_local:
                    angle_list = hand_angle(hand_local)
                    gesture_str = h_gesture(angle_list)
                    cv2.putText(frame, gesture_str, (0, 100), 0, 1.3, (0, 0, 255), 3)
                    if gesture_str == "Pistol":
                        status.append(1)
                    elif gesture_str == "Six":
                        status.append(2)
                    elif gesture_str == "Two":
                        status.append(3)
                    elif gesture_str == "Fist":
                        status.append(4)
        cv2.imshow("Group 8 Demo", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
        
        
        old_status =  0
        for i in status:
            if i == old_status:
                status.pop()
                
            else:
                old_status = i
                if i == 1:
                    driver.fullscreen_window()
                elif i ==2:
                    driver.set_window_size(1000, 800)
                elif i==3:
                    driver.refresh()  
                elif i ==4:
                    # button = driver.find_element_by_id('bt')
                    # driver.find_element_by_id('bt').click()
                    # x_path = "//button[@title='next']"
                    # button = driver.find_element_by_xpath(x_path)
                    # button.click()
                    pass
                status.pop()
                    
        
        
    cap.release()


if __name__ == "__main__":
    detect()
