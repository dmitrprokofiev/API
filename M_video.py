from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
# chrome_options.add_argument('start-maximized')
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(executable_path='/home/dmitry/PycharmProjects/lesson_5/chromedriver', options=chrome_options)

driver.get("https://www.mvideo.ru/")


def scroll_down():
    body = driver.find_element_by_css_selector('body')
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(3)

def scroll_right():
    while True:
        try:
            button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='accessories-carousel-wrapper ']//a[@class='next-btn c-btn c-btn_scroll-horizontal c-btn_icon i-icon-fl-arrow-right']")))
            button.click()
        except:
            break


scroll_down()

bestsellers = driver.find_elements_by_css_selector("ul.accessories-product-list")
for i in bestsellers:
    print(i.find_element_by_css_selector("a.fl-product-tile-title__link sel-product-tile-title").json())



