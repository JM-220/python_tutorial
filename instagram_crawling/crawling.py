#  instagram crawling... 실패

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # keyboard 의 누를 때 입력값이 저장되어있는 클래스 ex) keys.RETURN
from bs4 import BeautifulSoup
import time


id = "hwang.jaemoo"
pw = "vlzkcb1423."

options = webdriver.ChromeOptions()
options.add_argument('--headless')        # Head-less 설정
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# 원하는 User-Agent 값을 설정합니다.
user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
options.add_argument('user-agent=' + user_agent)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

# 사이트 접속 후 로그인
driver.get("https://www.instagram.com/")
driver.implicitly_wait(10)

inputId = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
driver.implicitly_wait(10)
inputPw = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
driver.implicitly_wait(10)
loginButton= driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]")
driver.implicitly_wait(10)

inputId.send_keys(id)
driver.implicitly_wait(10)
inputPw.send_keys(pw)
driver.implicitly_wait(10)

loginButton.click()
time.sleep(5)
htmlCode = driver.page_source

# 검색창에서 원하는 이름 검색
# searchName = input("검색 : ")

# searchButton = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div")
# driver.implicitly_wait(10)
# searchButton.click()
# driver.implicitly_wait(10)

# inputSpace = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input")
# inputSpace.send_keys(searchName)

# htmlCode = driver.page_source

# 여기서부터 오류 -> 아마도 주소로 직접 접근해서 코드가 일부 누락된 듯함. 처음부터 끝까지 검색을 통해서 접근해보자. 11/08
# followerButton = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a")
# followButton = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a")
# driver.implicitly_wait(10)

# followerButton.click()
# time.sleep(0.5)
# followerListTag = driver.find_element(By.XPATH,"/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div")
# time.sleep(0.5)
# topOfTheList = driver.find_element(By.XPATH,"/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[2]/div/div/div/div/div/a/div/div/span")
# name = topOfTheList.text
# driver.implicitly_wait(10)

driver.quit()
print(htmlCode)
