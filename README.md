# SeleniumMoveCursor
Moving cursor to element in browser run by selenium webdriver.
Works for chrome and firefox browser maximized or minimized. Method to use is move_to_element.

**Preconditions**
- Web element is visible on browser (scroll should be done before calling method move_to_element)

**Parameters for method move_to_element**
- driver - WebDriver
- element - WebElement
- display_scaling - Display scaling (100, 125, 150 or 175 %) need to be given when calling method move_to_element.
Default is 100.
This info can be found in display settings.

- chrome_info_bar_shown - Is shown chrome infobar with text: "Chrome is being controlled by automated test software"


**How to use method for moving cursor to web element (move_to_element):**

from selenium import webdriver
from selenium_move_cursor.MouseActions import move_to_element_chrome

driver = webdriver.Chrome(chrome_options=chrome_options)

driver.maximize_window()

driver.get("https://www.google.com/")
element = driver.find_elements_by_css_selector("input[class='gNO89b']")[1]


move_to_element_chrome(driver, element, display_scaling=100, chrome_info_bar_shown=True)