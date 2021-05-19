from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

chrome_options = Options()
chrome_options.add_argument('start-maximized')

driver = webdriver.Chrome(executable_path='/home/dmitry/PycharmProjects/lesson_5/chromedriver', options=chrome_options)

driver.get("https://mail.ru/")


