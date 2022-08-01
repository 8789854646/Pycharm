#
# from selenium.webdriver import Chrome
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.common.by import By
# from time import sleep
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# driver = Chrome(r"C:\Users\kushw\Downloads\chromedriver_win32 (1)\chromedriver.exe")
# driver.get("http://demowebshop.tricentis.com/")
# driver.maximize_window()
# sleep(3)
# class _visibility_of_element_located(visibility_of_element_located):
#     def __int__(self, locator):
#         super().__init__(locator)
#     def __call__(self, driver):
#         print("Calling __call__ method of child class")
#         result = super().__call__(driver)
#         if isinstance(result, WebElement):
#             return result.is_enabled()
#         else:
#             return False
#
# def _wait(func):
#     def wrapper(*args, **kwargs):
#         locator = args[0]
#         w = WebDriverWait(driver, 20)
#         v = _visibility_of_element_located(locator)
#         w.until(v, message="Progress bar was not located even after 20 seconds")
#         return func(*args, **kwargs)
#     return wrapper
#
# @_wait
# def click_element(locator):
#     driver.find_element(*locator).click()
#
# @_wait
# def enter_text(locator, *, value):
#     driver.find_element(*locator).clear()
#     driver.find_element(*locator).send_keys(value)
#
# @_wait
# def select_item(locator, *, item):
#     element = driver.find_element(*locator)
#     s = Select(element)
#     if isinstance(item, str):
#         s.select_by_visible_text(item)
#     elif isinstance(item, int):
#         s.select_by_index(item)
#     else:
#         raise Exception
#
# click_element((By.LINK_TEXT,"Register"))
# click_element((By.ID, "gender-male"))
# enter_text((By.ID, "FirstName"), value ="vivek")
# enter_text((By.ID, "LastName"), value = "kumar")
# enter_text((By.NAME, "Email"), value = "vivek@gmail.com")
# enter_text((By.ID, "Password"), value = "password123")
# enter_text((By.ID, "ConfirmPassword"),value = "password123")
# click_element((By.ID, "register-button"))

