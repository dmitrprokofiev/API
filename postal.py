from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
# chrome_options.add_argument('start-maximized')
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(executable_path='/home/dmitry/PycharmProjects/lesson_5/chromedriver', options=chrome_options)

driver.get("https://mail.ru/")

form = driver.find_element_by_name('login')
form.send_keys('study.ai_172')
form.send_keys(Keys.ENTER)
time.sleep(1)
form = driver.find_element_by_name('password')
form.send_keys('NextPassword172!')
form.send_keys(Keys.ENTER)
time.sleep(5)



def mail():
    message = driver.find_elements_by_class_name("llc js-tooltip-direction_letter-bottom js-letter-list-item llc_normal")
    return message

def scroll_down():
    body = driver.find_element_by_css_selector('body')
    for i in range(50):
        time.sleep(0.5)
        return body.send_keys(Keys.ARROW_DOWN)


print(mail())