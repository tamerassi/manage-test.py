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
# #
# #
# @pytest.fixture()
# def driver():
#     chrome_driver_binary = "tests/e2e/chromedriver.exe"
#     ser_chrome = ChromeService(chrome_driver_binary)
#     driver = webdriver.Chrome(ser_chrome)
#     yield driver
#     driver.close()
#
#
# def test_search_product(driver):
#     driver.get("http://127.0.0.1:8000/#/")
#     name_product = driver.find_element(By.CSS_SELECTOR,
#                                        "#root > div > main > div > div:nth-child(3) > div > div:nth-child(3) > div > div > a > div > strong").text
#     driver.find_element(By.NAME, "q").click()
#     driver.find_element(By.NAME, "q").send_keys(name_product)
#     time.sleep(3)
#     driver.find_element(By.CSS_SELECTOR, ".p-2").click()
#     time.sleep(2)
#     searched_product = driver.find_element(By.CSS_SELECTOR,
#                                            "#root > div > main > div > div > div > div:nth-child(1) > div > div > a > div > strong").text
#     assert searched_product == name_product
#     assert searched_product == "AVR ATMega328"
#
# #1