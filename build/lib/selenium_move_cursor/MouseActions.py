from win32api import GetMonitorInfo, MonitorFromPoint
import pyautogui
from win32api import GetSystemMetrics



def move_to_element_chrome(driver, element, displayScaling=125):
    """
    Move cursor to top right corner of element

    :param driver: WebDriver
    :param element: WebElement
    :param displayScaling: int
    :return:
    """
    tab_bar = int(72 * displayScaling / 100) #71 is chrome tab and address bar height when scaling is 100%
    x = _get_location_in_pixel(driver, element, tab_bar)["x"]
    y = _get_location_in_pixel(driver, element, tab_bar)["y"] + tab_bar
    pyautogui.moveTo(x, y, duration=1)


def _get_location_in_pixel(driver, element, tab_bar_height):
    """
    Get location of element that is shown in browser

    :param driver: WebDriver in selenium.webdriver.remote.webdriver
    :param element: webelement in selenium.webdriver.remote.webelement
    :return: dict
    """
    x_location_inside_of_browser = element.location["x"]
    y_location_inside_of_browser = element.location["y"]
    scroll_size = 0
    if _is_vertical_scroll_on_screen(driver):
        pass
    x_location_in_pixels = x_location_inside_of_browser*(GetSystemMetrics(0)-scroll_size)/(int(driver.find_element_by_tag_name("html").get_attribute("clientWidth")))
    monitor_info = GetMonitorInfo(MonitorFromPoint((0, 0)))
    monitor_area = monitor_info.get("Monitor")
    work_area = monitor_info.get("Work")
    task_bar = monitor_area[3] - work_area[3]
    hidden_pixels = driver.execute_script("return window.pageYOffset")
    y_location_in_pixels = (y_location_inside_of_browser-hidden_pixels)*(GetSystemMetrics(1)-tab_bar_height-task_bar)/int(driver.find_element_by_tag_name("html").get_attribute("clientHeight"))

    return {'x': x_location_in_pixels, 'y': y_location_in_pixels}


def _is_vertical_scroll_on_screen(driver):
    """
    Checks if scroll is shown

    :param driver: WebDriver
    :return: bool
    """
    vertical_scroll = False
    body_height = driver.execute_script("return document.getElementsByTagName('body')[0].clientHeight")
    inner_height = driver.execute_script("return window.innerHeight")
    if body_height > inner_height:
        vertical_scroll = True
    return vertical_scroll