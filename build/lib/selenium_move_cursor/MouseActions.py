from win32api import GetMonitorInfo, MonitorFromPoint
import pyautogui


def move_to_element_chrome(driver, element, display_scaling=100, chrome_info_bar_shown=True):
    """
    Deprecated, because works for chrome and firefox. Use move_to_element method.
    Left for backward compatibility.
    """
    tab_bar = _get_tab_size(driver, chrome_info_bar_shown, display_scaling)
    x = _get_location_in_pixel(driver, element, tab_bar, display_scaling)["x"]
    y = _get_location_in_pixel(driver, element, tab_bar, display_scaling)["y"] + tab_bar
    pyautogui.moveTo(x, y, duration=1)

def move_to_element(driver, element, display_scaling=100, chrome_info_bar_shown=True):
    """
    Move cursor to middle of element. Works for chrome and firefox

    :param driver: Chrome or Firefox driver
    :type driver: WebDriver
    :param element: Web element
    :type element:WebElement
    :param display_scaling: Display scaling percentage (100, 125, 150 or 175).
    This info can be found in 'Display settings'.
    :type display_scaling: int
    :return:
    """
    move_to_element_chrome(driver, element, display_scaling, chrome_info_bar_shown)

def _get_tab_size(driver, chrome_info_bar_shown, display_scaling):
    if "firefox" in driver.name:
        tab_bar = int(74 * display_scaling / 100)
    elif "chrome" in driver.name:
        if chrome_info_bar_shown:
            tab_bar = int(124 * display_scaling / 100)
        else:
            tab_bar = int(80 * display_scaling / 100)  # 80 is chrome tab and address bar height when scaling is 100%
    else:
        raise Exception("Not supported browser. Only chrome and firefox are supported.")
    return tab_bar

def _get_scroll_size(display_scaling):
    scroll_size = 16 * display_scaling / 100
    return scroll_size

def is_maximized(driver):
    return driver.get_window_position()['y'] == -8 and driver.get_window_position()['x'] == -8

def _get_location_in_pixel(driver, element, tab_bar_height, scaling):
    """
    Get location of element that is shown in browser

    :param driver: WebDriver in selenium.webdriver.remote.webdriver
    :param element: webelement in selenium.webdriver.remote.webelement
    :return: dict
    """
    x_location_inside_of_browser = element.location["x"]
    y_location_inside_of_browser = element.location["y"]
    scroll_size = _get_scroll_size(scaling)
    vertical_scroll_size = 0
    horizontal_scroll_size = 0
    if _is_vertical_scroll_on_screen(driver):
        vertical_scroll_size = scroll_size
    if _is_horizontal_scroll_on_screen(driver):
        horizontal_scroll_size = scroll_size

    browser_width_in_pixels = driver.get_window_size()['width'] * scaling/100
    browser_height_in_pixels = driver.get_window_size()['height'] * scaling / 100
    x_location_in_pixels = (x_location_inside_of_browser + element.size["width"]/2)*(browser_width_in_pixels-vertical_scroll_size)/(int(driver.find_element_by_tag_name("html").get_attribute("clientWidth"))) + driver.get_window_position()['x']
    monitor_info = GetMonitorInfo(MonitorFromPoint((0, 0)))
    monitor_area = monitor_info.get("Monitor")
    work_area = monitor_info.get("Work")
    task_bar = monitor_area[3] - work_area[3]
    hidden_pixels = driver.execute_script("return window.pageYOffset")
    y_location_in_pixels = (y_location_inside_of_browser+element.size["height"]/2-hidden_pixels)*(browser_height_in_pixels-tab_bar_height - horizontal_scroll_size)/int(driver.find_element_by_tag_name("html").get_attribute("clientHeight")) + driver.get_window_position()['y']

    return {'x': x_location_in_pixels, 'y': y_location_in_pixels}


def _is_horizontal_scroll_on_screen(driver):
    """
    Checks if scroll is shown

    :param driver: WebDriver
    :return: bool
    """
    horizontal_scroll = False
    scroll_width = driver.execute_script("return document.getElementsByTagName('html')[0].scrollWidth")
    inner_width = driver.execute_script("return window.innerWidth")
    print("check horisontal scrollbar...")
    if int(inner_width) < int(scroll_width):
        print("horisontal scrollbar exist")
        horizontal_scroll = True
    return horizontal_scroll


def _is_vertical_scroll_on_screen(driver):
    """
    Checks if scroll is shown

    :param driver: WebDriver
    :return: bool
    """
    vertical_scroll = False
    scroll_height = driver.execute_script("return document.getElementsByTagName('html')[0].scrollHeight")
    inner_height = driver.execute_script("return window.innerHeight")
    print("check vertical scrollbar...")
    if int(scroll_height) > int(inner_height):
        print("vertical scrollbar exist")
        vertical_scroll = True
    return vertical_scroll