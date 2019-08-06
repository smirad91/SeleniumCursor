# SeleniumMoveCursor
Moving cursor to element in browser run by selenium webdriver.
Currently works for chrome and firefox browser maximized. Method to use is move_to_element.

#Preconditions
- Chrome is run by selenium webdriver and is maximized
- Web element is visible on browser (scroll is done before calling method move_to_element)

#Parameters
- display_scaling - Display scaling (100, 125, 150 or 175 %) need to be given when calling method move_to_element.
This info can be found in display settings.

- chrome_info_bar_shown - Also if infobar is shown in chrome or not ("Chrome is being controlled by automated test software""),
 set in parameter chrome_info_bar_shown


#How to use method for moving cursor to web element (move_to_element):

from selenium import webdriver
from selenium_move_cursor.MouseActions import move_to_element_chrome

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobars")
driver = webdriver.Chrome(chrome_options=chrome_options)


driver.maximize_window()

driver.get("https://www.google.com/")
element = driver.find_elements_by_css_selector("input[class='gNO89b']")[1]


move_to_element_chrome(driver, element, display_scaling=100)