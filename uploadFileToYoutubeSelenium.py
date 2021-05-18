#Simple assignment
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(executable_path='geckodriver.exe')

url = "https://youtube.com/"
driver.get(url)

print(driver)

# elements = driver.find_elements_by_css_selector(".tp-yt-paper-button.size-small")
element = driver.find_element_by_xpath('//div[@id="end"]/div[@id="buttons"]/ytd-button-renderer')
element.click()