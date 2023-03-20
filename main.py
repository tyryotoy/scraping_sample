from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

import os


driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
driver.get('https://www.a8.net/')

media_login_id_element = driver.find_element(By.NAME,'login')
media_password_element = driver.find_element(By.NAME,'passwd')
media_login_id_element.send_keys(os.environ["A8_LOGIN_ID"])
media_password_element.send_keys(os.environ["A8_LOGIN_PASSWORD"])
media_password_element.submit()

driver.implicitly_wait(10)

driver.get_screenshot_as_file('./screenshots/login.png')

detail_report_btn = driver.find_element(By.LINK_TEXT, "詳細レポート").click()
