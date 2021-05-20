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
chrome_options.add_argument('start-maximized')

driver = webdriver.Chrome(executable_path='/home/dmitry/PycharmProjects/lesson_5/chromedriver', options=chrome_options)

driver.get("https://www.mvideo.ru/?utm_source=yandex&utm_medium=cpc&utm_campaign=ipr_Spb_Image_Name_Pure_search_desktop&utm_content=pid|21914267968_|cid|54501639|gid|4285483795|aid|9547781183|pos|premium1|key|mvideo|addphrases|no|dvc|desktop|region|10897|region_name|%d0%9c%d1%83%d1%80%d0%bc%d0%b0%d0%bd%d1%81%d0%ba%d0%b0%d1%8f%20%d0%be%d0%b1%d0%bb%d0%b0%d1%81%d1%82%d1%8c|coef_goal|0|desktop&utm_term=mvideo&reff=yandex_cpc_ipr_Spb_Image_Name_Pure_Search&_openstat=ZGlyZWN0LnlhbmRleC5ydTs1NDUwMTYzOTs5NTQ3NzgxMTgzO3lhbmRleC5ydTpwcmVtaXVt&yclid=2710185966102161678")

while True:
    try:
        button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='gallery-layout articles']//a[@class='next-btn c-btn c-btn_scroll-horizontal i-icon-fl-arrow-right']")))
        button.click()
    except:
        break
