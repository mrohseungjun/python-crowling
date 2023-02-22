import matplotlib.pyplot as plt
import matplotlib as mpl
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time

path = "D:\\JUNG\\util\\chromedriver_win32\\chromedriver.exe"
options = wd.ChromeOptions()
options.add_experimental_option('detach', True)
driver = wd.Chrome(path, options=options)
# driver.get("https://google.com")
r = driver.execute_script('return 100*50')
print(r)

