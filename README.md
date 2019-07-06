# SeleniumMoveCursor
Moving cursor to element in browser run by selenium webdriver.
Currently works for chrome browser, maximized. Method to use is move_to_element_chrome.

#Preconditions
- Chrome is run by selenium webdriver and is maximized
- Chrome infobar is disabled. Python code to achieve this:

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobars")
driver = webdriver.Chrome(chrome_options=chrome_options)

- Web element is visible on browser (scroll is done before calling method move_to_element_chrome)
- Display scaling (100, 125, 150 or 175 %) need to be given when calling method move_to_element_chrome. 
This info can be found in display settings.

#How to use method for moving cursor to web element (move_to_element_chrome):

from selenium import webdriver
from selenium_move_cursor.MouseActions import move_to_element_chrome

<!-- open chrome with disabled infobars -->
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobars")
driver = webdriver.Chrome(chrome_options=chrome_options)

<!-- maximize browser -->
driver.maximize_window()

driver.get("https://www.google.com/")
element = driver.find_elements_by_css_selector("input[class='gNO89b']")[1]

<!-- call method for moving cursor -->
move_to_element_chrome(driver, element, 125)