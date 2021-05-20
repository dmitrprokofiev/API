from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_argument('start-maximized')

driver = webdriver.Chrome(executable_path='/home/dmitry/PycharmProjects/lesson_5/chromedriver', options=chrome_options)

driver.get("https://mail.ru/")

form = driver.find_element_by_name('login')
form.send_keys('study.ai_172')
form.send_keys(Keys.ENTER)
time.sleep(1)
form = driver.find_element_by_name('password')
form.send_keys('NextPassword172!')
form.send_keys(Keys.ENTER)

try:
    time.sleep(3)
    letter = driver.find_elements_by_tag_name('html')
    # actions = ActionChains(driver)
    # letter.send_keys(Keys.PAGE_DOWN)
except:
    driver.close()
