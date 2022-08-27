# import time
#
# import pytest
#
# from selenium import webdriver
# from selenium.webdriver import Keys, ActionChains
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options as FireFoxOptions
# from selenium.webdriver.firefox.service import Service as FirefoxService
#
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
#
# @pytest.fixture()
# def driver():
#     chrome_driver_binary = "chromedriver.exe"
#     ser_chrome = ChromeService(chrome_driver_binary)
#     driver = webdriver.Chrome(service=ser_chrome)
#     yield driver
#     driver.close()
#
#
# def test_admin_user_edit_product(driver):
#     driver.get("http://127.0.0.1:8000/#/")
#     driver.maximize_window()
#     driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
#     driver.find_element(By.ID, "email").click()
#     driver.find_element(By.ID, "email").send_keys("tamerassi1@gmail.com")
#     driver.find_element(By.ID, "password").click()
#     driver.find_element(By.ID, "password").send_keys("assi12345")
#
#     driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
#     time.sleep(8)
#     driver.execute_script(
#         "document.getElementById('adminmenu').scrollIntoView();")
#     driver.find_element(By.ID, "adminmenu").click()
#     driver.find_element(By.LINK_TEXT, "Products").click()
#     time.sleep(2)
#     driver.execute_script(
#         "document.querySelector('#root > div > main > div > div:nth-child(2) > div > table > tbody > tr:nth-child(4) > td:nth-child(6) > a').scrollIntoView();")
#     time.sleep(2)
#     driver.find_element(By.CSS_SELECTOR,
#                         "#root > div > main > div > div:nth-child(2) > div > table > tbody > tr:nth-child(4) > td:nth-child(6) > a").click()
#     driver.execute_script("window.scrollTo(0,217)")
#     driver.find_element(By.CSS_SELECTOR, ".justify-content-md-center").click()
#     driver.find_element(By.ID, "countinstock").send_keys("")
#     time.sleep(2)
#     driver.execute_script("window.scrollTo(0,487)")
#     driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div > div > div > form > button").click()
#     time.sleep(1)
#     driver.execute_script(
#         "document.querySelector('#root > div > main > div > div:nth-child(2) > div > table > tbody > tr:nth-child(4) > td:nth-child(6) > a').scrollIntoView();")
#     time.sleep(1)
#     driver.find_element(By.CSS_SELECTOR,
#                         "#root > div > main > div > div:nth-child(2) > div > table > tbody > tr:nth-child(4) > td:nth-child(6) > a").click()
#     stock_input = driver.find_element(By.ID, "countinstock").get_attribute('value')
#     assert stock_input == "110"
#
#
