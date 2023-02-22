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
print(all_videos)

time.sleep(2)
#제목, 재생시간 ,조회수
datas = []
for video in  all_videos:
  title = video.find_element(By.ID, 'video-title').text
  video_time = video.find_element(By.CSS_SELECTOR,
  '.style-scope ytd-thumbnail-overlay-time-status-renderer').text.strip()

  video_num =video.find_element(By.XPATH,'//*[@id="metadata-line"]/span[1]').text
  datas.append([title,video_time,video_num])

print(datas)  

#########

