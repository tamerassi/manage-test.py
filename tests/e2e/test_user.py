# import time
#
# import pytest
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options as FireFoxOptions
# from selenium.webdriver.firefox.service import Service as FirefoxService
#
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# @pytest.fixture()
# def driver():
#     chrome_driver_binary = "chromedriver.exe"
#     ser_chrome = ChromeService(chrome_driver_binary)
#     driver = webdriver.Chrome(chrome_driver_binary)
#     yield driver
#     driver.close()
#
#
# '''
# testing user
#
# '''
#
#
# def test_user_login(driver):
#     driver.get("http://127.0.0.1:8000/#/")
#     driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
#     driver.maximize_window()
#     # time.sleep(2)
#     driver.find_element(By.ID, "email").click()
#     driver.find_element(By.ID, "email").send_keys("tamer.tester@gmail.com")
#     driver.find_element(By.ID, "password").click()
#     driver.find_element(By.ID, "password").send_keys("assi12345")
#     driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
#     time.sleep(3)
#     username = driver.find_element(By.CSS_SELECTOR, "#username").text
#     time.sleep(3)
#     assert username == "TAMER"
#
#
# def test_user_create_account(driver):
#     driver.get("http://127.0.0.1:8000/#/")
#     driver.maximize_window()
#     driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
#     # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#root > div > main > div > div > div > div > div > a"))).click()
#     driver.execute_script(
#         "document.querySelector('#root > div > main > div > div > div > div > div > a').scrollIntoView();")
#     register = driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div > div > div > div > a")
#     time.sleep(5)
#     register.click()
#     time.sleep(5)
#     driver.find_element(By.ID, "name").click()
#     driver.find_element(By.ID, "name").send_keys("assi")
#     driver.find_element(By.ID, "email").click()
#     driver.find_element(By.ID, "email").send_keys("assi7@gmail.com")
#     driver.find_element(By.ID, "password").click()
#     driver.find_element(By.ID, "password").send_keys("assi12345")
#     driver.find_element(By.ID, "passwordConfirm").click()
#     driver.find_element(By.ID, "passwordConfirm").send_keys("assi12345")
#     driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
#     time.sleep(4)
#     driver.execute_script("window.scrollTo(0,198.6666717529297)")
#     username = driver.find_element(By.CSS_SELECTOR, "#username").text
#     time.sleep(3)
#     assert username == "ASSI"
#
#
# def test_user_create_account_for_existed_account(driver):
#     driver.get("http://127.0.0.1:8000/#/")
#     driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
#     # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#root > div > main > div > div > div > div > div > a"))).click()
#     driver.execute_script(
#         "document.querySelector('#root > div > main > div > div > div > div > div > a').scrollIntoView();")
#     register = driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div > div > div > div > a")
#     time.sleep(3)
#     register.click()
#     # time.sleep(5)
#     driver.find_element(By.ID, "name").click()
#     driver.find_element(By.ID, "name").send_keys("assi")
#     driver.find_element(By.ID, "email").click()
#     driver.find_element(By.ID, "email").send_keys("assi@gmail.com")
#     driver.find_element(By.ID, "password").click()
#     driver.find_element(By.ID, "password").send_keys("assi12345")
#     driver.find_element(By.ID, "passwordConfirm").click()
#     driver.find_element(By.ID, "passwordConfirm").send_keys("assi12345")
#     driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
#     time.sleep(2)
#     # driver.execute_script("window.scrollTo(0,198.6666717529297)")
#     error_note = driver.find_element(By.CSS_SELECTOR,
#                                      "#root > div > main > div > div > div > div.fade.alert.alert-danger.show").text
#     assert error_note == "User with this email is already registered"
#
#
# def test_user_create_account_with_incorrect_email_format(driver):
#     driver.get("http://127.0.0.1:8000/#/")
#     driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
#     # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#root > div > main > div > div > div > div > div > a"))).click()
#     driver.execute_script(
#         "document.querySelector('#root > div > main > div > div > div > div > div > a').scrollIntoView();")
#     register = driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div > div > div > div > a")
#     time.sleep(3)
#     register.click()
#     # time.sleep(5)
#     driver.find_element(By.ID, "name").click()
#     driver.find_element(By.ID, "name").send_keys("assi")
#     driver.find_element(By.ID, "email").click()
#     driver.find_element(By.ID, "email").send_keys("t")
#     driver.find_element(By.ID, "password").click()
#     driver.find_element(By.ID, "password").send_keys("assi12345")
#     driver.find_element(By.ID, "passwordConfirm").click()
#     driver.find_element(By.ID, "passwordConfirm").send_keys("assi12345")
#     driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
#     time.sleep(2)
#     # driver.execute_script("window.scrollTo(0,198.6666717529297)")
#     assert driver.current_url == "http://127.0.0.1:8000/#/register?redirect=/"
