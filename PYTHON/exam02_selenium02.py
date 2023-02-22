from selenium import webdriver as wd
from selenium.webdriver.common.by import By

# 셀레니움 사용법
path = "C:\\Users\\admin\\Downloads\\chromedriver_win32\\chromedriver.exe"
options = wd.ChromeOptions()
# options.add_experimental_option('excludeSwitches',['enable-logging'])
options.add_experimental_option('detach',True)
driver = wd.Chrome(path,options=options)
driver.get('https://naver.com')

driver.find_element(By.ID,'query').send_keys('파이썬') # 셀레니움 문법
driver.find_element(By.ID,'search_btn').click()




