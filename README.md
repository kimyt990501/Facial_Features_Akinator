# 얼굴 특징 아키네이터
인물의 얼굴 특징 및 기타 특징 데이터를 사용하여 누구인지 맞추는 프로그램
- 베이즈 정리 기반 분류기를 적용시킨 아키네이터
- Bayesian theorem-based Akinator with Python

## 파일 명
- data_crawling.py (필요한 데이터 크롤링)
- data_preproc.py (데이터 전처리)
- cv_img_analysis.py (인물 이미지를 통해 특징점 추출)
- facial_features_akinator.py (얼굴 특징 데이터를 통해 아키네이터 구현)

## 개발환경
- IDE: Visual Studio Code
- Version: python 3.8

## 기술 스택
- 언어: Python
- 라이브러리: cv2(OpenCV), selenium, imutils, dlib 

## 절차
- 필요한 인물의 얼굴 이미지와 정보를 웹사이트에서 크롤링해온다
- 크롤링해온 데이터 중 이미지 파일을 통해 파이썬 OpenCV 라이브러리로 얼굴 특징점들을 가져온다
- 각 특징점들을 통해 얼굴에서 눈, 코, 입의 얼굴 크기 대비 비율을 구하여 해당 인물의 정보에 추가
- 각 데이터를 하나의 파일로 합친다
- 해당 파일을 불러와 얼굴 특징 아키네이터 구현

## 데이터 전처리 과정
- 일정한 각도에서 찍은 여러 명의 단독 사진이 필요했는데 그에 부합하는 사진으로 야구 선수들의 프로필 사진을 선택했으며 해당 이미지들은 KBO 공식 홈페이지에서 쉽게 구할 수 있다
- KBO 공식 홈페이지에서 데이터를 크롤링하기 위해서는 해당 사이트의 페이지 소스를 가져와야 했다, 하지만 해당 사이트가 동적사이트였기 때문에 Selenium 을 사용하였다
- <https://www.koreabaseball.com/Player/Search.aspx>
- 해당 사이트에서 인물들의 이름, 얼굴 이미지, 키, 생년월일, 포지션 정보를 가져와 데이터프레임에 넣어준 후 csv 파일로 저장하였다 player_info.csv
- 다음으로 이미지 파일을 OpenCV 라이브러리를 통해 얼굴의 특징점 좌표를 뽑아와서 아래와 같이 여러 특징으로 분류하여 저장하였다 samsung_face.csv
    - eye_width_rate: 눈의 너비와 얼굴 너비의 비율
    - mouth_width_rate: 입의 너비와 얼굴 너비의 비율
    - bet_eyes_rate: 두 눈 사이 간격과 얼굴 너비의 비율
    - nose_width_rate: 코 너비와 코 길이의 비율
    - lip_rate: 입술 두께와 얼굴 세로 길이의 비율
    - eye_height_rate: 눈의 세로 길이와 얼굴 세로 길이의 비율
- (하지만 위 특징들이 인물을 구분할 수는 있지만 아직 정확하게 전부 구분하기는 힘들어서 추후 다른 방식으로 수정할 계획이다)
- 위 데이터들을 하나의 데이터프레임으로 합친 후 csv 파일로 저장하였다. samsung_facialfeatures.csv

## 프로그램 동작 과정
- 사용자는 본인이 인물 하나를 생각한다
- 프로그램은 사용자에게 질문들을 하며 답을 입력해나간다
- 질문에 대한 답으로는
- 예, 아니오, 모르겠습니다, 그럴겁니다, 아닐겁니다
- 이렇게 총 5가지 선택지가 있다
- 질문을 다 끝낸 프로그램은 사용자가 입력한 답을 토대로 사용자가 생각하는 인물이 누구인지 출력하며 프로그램을 종료한다
- 프로그램 예시화면은 아래와 같다
- ![t](https://github.com/kimyt990501/Facial_Features_Akinator/assets/50610894/d380b9b1-d81d-418a-aae9-5b9a40deb44f)

## 아쉬운 점
- 얼굴 특징이 명확한 인물은 정확도가 높지만 그렇지 않은 인물들은 정확도가 낮은 편이다

## 추가할 사항
- UI를 추가해서 웹이든 실행파일이든 결과물로 만들 예정
- 못 맞춘 경우에 대해서 기능 추가 예정
- 보다 정확한 인물 구분을 위한 다른 특징을 추가하거나 대체하여 꾸준히 업데이트할 예정
