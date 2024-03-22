import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.headless = True
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver, 4)

driver.maximize_window()

driver.get('https://www.saucedemo.com/')

driver.find_element(By.ID, "user-name").send_keys('standard_user')
driver.find_element(By.ID, "password").send_keys('secret_sauce')
driver.find_element(By.ID, "login-button").click()

wait.until(EC.element_to_be_clickable((By.ID, 'add-to-cart-sauce-labs-backpack'))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt'))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'add-to-cart-sauce-labs-onesie'))).click()
driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()

wait.until(EC.element_to_be_clickable((By.ID, 'checkout'))).click()

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.checkout_info')))
driver.find_element(By.ID, "first-name").send_keys('Сотов')
driver.find_element(By.ID, "last-name").send_keys('Александр')
driver.find_element(By.ID, "postal-code").send_keys('192000')
driver.find_element(By.ID, "continue").click()

def test_total_cost():
    total = driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
    assert total == 'Total: $58.29'





