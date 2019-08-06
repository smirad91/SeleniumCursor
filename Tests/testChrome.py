from selenium import webdriver
from selenium_move_cursor.MouseActions import move_to_element_chrome

driver = webdriver.Chrome()


driver.maximize_window()

driver.get("https://www.google.com/")
element = driver.find_elements_by_css_selector("input[class='gNO89b']")[1]


move_to_element_chrome(driver, element, display_scaling=100, chrome_info_bar_shown=True)
