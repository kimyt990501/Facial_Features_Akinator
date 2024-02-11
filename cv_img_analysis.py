import numpy as np
import dlib
import pandas as pd
import imutils
import cv2
import os

# 얼굴 좌표용 배열
RIGHT_EYE = list(range(36, 42))
LEFT_EYE = list(range(42, 48))
MOUTH = list(range(48, 68))
NOSE = list(range(27, 36))
EYEBROWS = list(range(17, 27))
JAWLINE = list(range(1, 17))
ALL = list(range(0, 68))
EYES = list(range(36, 48))

list = []

# 데이터 파일과 이미지 파일 경로
predictor_file = 'C:\\Users\\user\\Desktop\\github_repo\\Facial_Features_Akinator\\shape_predictor_68_face_landmarks.dat'
os.chdir('./data/samsung')

file_names = os.listdir()

# 얼굴 특징값 식별
for filename in file_names:
    
    birth_num = os.path.splitext(filename)[0]
    
    image_link = birth_num + '.png'

    detector = dlib.get_frontal_face_detector()

    predictor = dlib.shape_predictor(predictor_file)

    image = cv2.imread(image_link)
    image = imutils.resize(image, width=500)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    rects = detector(gray, 1)
    #print("Number of faces detected: {}".format(len(rects)))


    for (i, rect) in enumerate(rects):
        points = np.matrix([[p.x, p.y] for p in predictor(gray, rect).parts()])
        show_parts = points[ALL]
        for (i, point) in enumerate(show_parts):
            x = point[0,0]
            y = point[0,1]
            cv2.circle(image, (x, y), 1, (0, 255, 255), -1)
            cv2.putText(image, "{}".format(i + 1), (x, y - 2),
            cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), 1)
    #cv2.imshow("Face Landmark", image)
    #cv2.waitKey(0)

    # Facial Features 얼굴 특징 값
    bet_eyes = show_parts[42, 0] - show_parts[39, 0]
    face_width = show_parts[16, 0] - show_parts[0, 0]
    face_height = show_parts[8, 1] - show_parts[27, 1]
    eye_width = show_parts[39, 0] - show_parts[36, 0]
    eye_height = show_parts[41, 1] - show_parts[37, 1]
    nose_height = show_parts[33, 1] - show_parts[27, 1]
    nose_width = show_parts[35, 0] - show_parts[31, 0]
    mouth_width = show_parts[54, 0] - show_parts[48, 0]
    mouth_height = show_parts[58, 1] - show_parts[50, 1]
    
    # 얼굴 특징 값을 이용한 비율 값
    eye_width_rate = eye_width / face_width # 눈의 너비 와 얼굴 너비의 비율
    mouth_width_rate = mouth_width / face_width # 입의 너비와 얼굴 너비의 비율
    bet_eyes_rate = bet_eyes / face_width # 눈 사이 간격과 얼굴 너비의 비율
    nose_width_rate = nose_width / nose_height # 코 너비와 코 길이의 비율
    lip_rate = mouth_height / face_height # 입의 세로 길이와 얼굴 세로 길이의 비율
    eye_height_rate = eye_height / face_height # 눈의 세로 길이와 얼굴 세로 길이의 비율
    
    #image_link[13:21]
    temp = [birth_num, '%0.3f' % bet_eyes_rate, '%0.3f' % eye_width_rate, '%0.3f' % eye_height_rate, '%0.3f' % nose_width_rate, '%0.3f' % mouth_width_rate, '%0.3f' % lip_rate]
    list.append(temp)

df = pd.DataFrame(list)
df.columns = ['birth', 'bet_eyes_rate', 'eye_width_rate', 'eye_height_rate', 'nose_width_rate', 'mouth_width_rate', 'lip_rate']
#print(df)

df.to_csv('C:\\Users\\user\\Desktop\\github_repo\\Facial_Features_Akinator\\data\\samsung_face.csv')