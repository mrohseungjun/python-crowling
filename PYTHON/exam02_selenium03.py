from selenium import webdriver as wd
from selenium.webdriver.common.by import By

path = "C:\\Users\\admin\\Downloads\\chromedriver_win32\\chromedriver.exe"
options = wd.ChromeOptions()
options.add_experimental_option('detach',True)
driver = wd.Chrome(path,options=options)
driver.get('https://www.youtube.com/c/paikscuisine/videos')
# /html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[1]
# /html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[1]
items = driver.find_elements(By.XPATH,'//*[@id="contents"]/ytd-rich-grid-row[1]')
for i in items:
    title = i.find_element(By.XPATH,'//*[@id="video-title"]')
    item = i.text
    print(title)