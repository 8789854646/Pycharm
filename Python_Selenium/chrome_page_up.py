from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver = Chrome(r"C:\Users\kushw\PycharmProjects\Pycharm Selenium\chromedriver.exe")
driver.get("https://www.flipkart.com/")
driver.maximize_window()
sleep(3)
driver.find_element("xpath", "//button[text()='✕']").click()
sleep(3)
lgn_btn = driver.find_element("xpath", "//a[text()='Login']")
action = ActionChains(driver)
action.move_to_element(lgn_btn).perform()
sleep(3)
driver.back()
sleep(3)
driver.refresh()
sleep(3)
driver.forward()

