# import time
#
# import pytest
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# @pytest.fixture()
# def driver():
#     driver = webdriver.Chrome(Service(ChromeDriverManager().install()))
#     yield driver
#     driver.close()
#
#
# def test_search_product(driver):
#     driver.get("http://127.0.0.1:8000/#/")
#     name_product = driver.find_element(By.CSS_SELECTOR,
#                                        "#root > div > main > div > div:nth-child(3) > div > div:nth-child(3) > div > div > a").text
#     driver.find_element(By.NAME, "q").click()
#     driver.find_element(By.NAME, "q").send_keys(name_product)
#     time.sleep(3)
#     driver.find_element(By.CSS_SELECTOR, ".p-2").click()
#     time.sleep(2)
#     searched_product = driver.find_element(By.CSS_SELECTOR,
#                                            "#root > div > main > div > div > div > div:nth-child(1) > div > div > a > div > strong").text
#     assert searched_product == name_product
#     assert name_product == "AVR ATMega328"
#
