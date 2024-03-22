import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.headless = True
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)

driver.maximize_window()
driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
time = 45
delay = driver.find_element(By.CSS_SELECTOR, "#delay")
delay.clear()
delay.send_keys(time)
driver.find_element(By.XPATH, "//span[text()='7']").click()
driver.find_element(By.XPATH, "//span[text()='+']").click()
driver.find_element(By.XPATH, "//span[text()='8']").click()
driver.find_element(By.XPATH, "//span[text()='=']").click()
sleep(time)
def test_calculator_result():
    result = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert result == '15'