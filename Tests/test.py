import time

from selenium import webdriver
from selenium_move_cursor.MouseActions import move_to_element_chrome


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobars")
driver = webdriver.Chrome(chrome_options=chrome_options)


driver.maximize_window()

driver.get("https://www.google.com/")
time.sleep(5)
element = driver.find_elements_by_css_selector("input[class='gNO89b']")[1]


move_to_element_chrome(driver, element, display_scaling=100)
