import matplotlib.pyplot as plt
import matplotlib as mpl
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time

path = "D:\\JUNG\\util\\chromedriver_win32\\chromedriver.exe"
options = wd.ChromeOptions()
options.add_experimental_option('detach', True)
driver = wd.Chrome(path, options=options)
driver.get("https://www.youtube.com/c/paikscuisine/videos")

# all_videos = driver.find_elements(By.ID, "dismissible")
all_videos = driver.find_elements(By.CSS_SELECTOR, "#dismissible")

body_tag = driver.find_element(By.TAG_NAME, 'body')
# print(body_tag)
# 스크롤이 1번 진행된다.
from selenium.webdriver.common.keys import Keys
body_tag.send_keys(Keys.END)

# 화면 길이 확인하기
# document.documentElement.scrollHeight :화면길이
# print(driver.execute_script('return document.documentElement.scrollHeight'))

while True:
  last_height = driver.execute_script('return document.documentElement.scrollHeight')
  print('last_height : ', last_height)
  # 10번 스크롤하기
  for i in range(10):
    body_tag.send_keys(Keys.END)
    time.sleep(1)
    new_height = driver.execute_script('return document.documentElement.scrollHeight')
    print('new_height : ', new_height)

  if last_height == new_height:
    print("화면길이 같아서 반복 종료")
    break
  print('='*100)  