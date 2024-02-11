#%%
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import urllib.request
from selenium.common.exceptions import NoSuchElementException

import warnings
warnings.filterwarnings('ignore')

# 선수 정보 및 이미지 크롤링
list = []

driver = webdriver.Chrome()
url = 'https://www.koreabaseball.com/Player/Search.aspx'
driver.get(url)

for i in range(1, 21):
    # 팀선택
    driver.find_element(By.XPATH, "//*[@id='cphContents_cphContents_cphContents_ddlTeam']/option[9]").click()

    sleep(0.5) # 0.5초 대기

    # 페이지 선택
    
    #driver.find_element(By.XPATH, '//*[@id="cphContents_cphContents_cphContents_ucPager_btnNo5"]').click()
    
    sleep(0.5)
    
    # 선수 선택
    driver.find_element(By.XPATH, '//*[@id="cphContents_cphContents_cphContents_udpRecord"]/div[2]/table/tbody/tr[' + str(i) + ']/td[2]/a').click()

    # 이미지 링크 추출 및 선수 이름, 생일 링크 추출
    
    # 1군일 경우
    try:
        #imgUrl = driver.find_element(By.XPATH, '//*[@id="cphContents_cphContents_cphContents_playerProfile_imgProgile"]').get_attribute("src")
        nameUrl = driver.find_element(By.XPATH, '//*[@id="cphContents_cphContents_cphContents_playerProfile_lblName"]')
        birthUrl = driver.find_element(By.XPATH, '//*[@id="cphContents_cphContents_cphContents_playerProfile_lblBirthday"]')
        leftrightposUrl = driver.find_element(By.XPATH, '//*[@id="cphContents_cphContents_cphContents_playerProfile_lblPosition"]')
        heightUrl = driver.find_element(By.XPATH, '//*[@id="cphContents_cphContents_cphContents_playerProfile_lblHeightWeight"]')
    # 퓨쳐스리그인 경우
    except NoSuchElementException:
        #imgUrl = driver.find_element(By.XPATH, '//*[@id="cphContents_cphContents_cphContents_ucPlayerProfile_imgProfile"]').get_attribute("src")
        nameUrl = driver.find_element(By.XPATH, '//*[@id="cphContents_cphContents_cphContents_ucPlayerProfile_lblName"]')
        birthUrl = driver.find_element(By.XPATH, '//*[@id="cphContents_cphContents_cphContents_ucPlayerProfile_lblBirthday"]')
        leftrightposUrl = driver.find_element(By.XPATH, '//*[@id="cphContents_cphContents_cphContents_ucPlayerProfile_lblPosition"]')
        heightUrl = driver.find_element(By.XPATH, '//*[@id="cphContents_cphContents_cphContents_ucPlayerProfile_lblHeightWeight"]')
    
    name = nameUrl.text # 이름
    year = birthUrl.text[:4] # 년
    month = birthUrl.text[6:8] # 월
    day = birthUrl.text[10:12] # 일
    position = leftrightposUrl.text[:-6] # 포지션
    height = heightUrl.text[:3] # 키
    birth = year + month + day
    temp = [name, birth, position, height]
    list.append(temp) # 리스트에 정보 저장
    
    # 이미지 저장
    #urllib.request.urlretrieve(imgUrl, "data/samsung/" + birth + ".png")

    driver.back() # 뒤로가기
'''
# 선수 정보 데이터프레임에 저장 후 csv 파일 추출
df = pd.DataFrame(list)
df.columns = ['name', 'birth', 'position', 'height']
df.to_csv('data/player_info.csv', encoding='euc-kr')
'''
# %%
