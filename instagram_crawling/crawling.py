from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # keyboard 의 누를 때 입력값이 저장되어있는 클래스 ex) keys.RETURN
from bs4 import BeautifulSoup
import time


id = "hwang.jaemoo"
pw = "vlakcb1423."

options = webdriver.ChromeOptions()
options.add_argument('--headless')        # Head-less 설정
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)
time.sleep(1)

driver.get("https://www.instagram.com/")
time.sleep(1)

inputId = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
time.sleep(1)
inputPw = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
time.sleep(1)
loginButton= driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]")
time.sleep(1)

inputId.send_keys(id)
time.sleep(1)
inputPw.send_keys(pw)
time.sleep(1)

loginButton.click()
time.sleep(1)

driver.get("https://www.instagram.com/hm_son7/")
time.sleep(1)
# 여기서부터 오류 -> 아마도 주소로 직접 접근해서 코드가 일부 누락된 듯함. 처음부터 끝까지 검색을 통해서 접근해보자. 11/08
followerButton = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a")
followButton = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a")
time.sleep(1)

followerButton.click()
time.sleep(0.5)
followerListTag = driver.find_element(By.XPATH,"/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div")
time.sleep(0.5)
topOfTheList = driver.find_element(By.XPATH,"/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[2]/div/div/div/div/div/a/div/div/span")
name = topOfTheList.text
time.sleep(1)

driver.quit()
print(name)