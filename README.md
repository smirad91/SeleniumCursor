# SeleniumMoveCursor
Moving cursor to element in browser run by selenium webdriver.
Currently works for chrome browser, maximized and with no scroll (vertical and horizontal).
Precondition is to have chrome browser infobar disabled. Python code to achieve this:

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobars")
driver = webdriver.Chrome(chrome_options=chrome_options)

Also display scaling (percentage) need to be given when calling method move_to_element_chrome. 
This info can be found in display settings.

#How to use it:
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