from selenium import webdriver
from selenium_move_cursor.MouseActions import move_to_element


driver = webdriver.Firefox()


driver.maximize_window()

driver.get("https://www.google.com/")

element = driver.find_elements_by_css_selector("input[class='gNO89b']")[1]


move_to_element(driver, element, display_scaling=100)