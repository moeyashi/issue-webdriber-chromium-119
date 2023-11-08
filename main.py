import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

print("start")

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--user-agent=selenium')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-zygote')
options.add_argument('--single-process')
driver = webdriver.Chrome(options=options)
driver.get("https://www.selenium.dev/")
h1 = driver.find_element(by=By.TAG_NAME, value="h1")
print(h1.text)
# これもエラー
print(driver.current_url)
print("finish")
