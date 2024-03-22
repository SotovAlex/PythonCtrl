import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.headless = True
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)

driver.maximize_window()
driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys('Иван')
driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys('Петров')
driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys('Ленина, 55-3')
driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys('test@skypro.com')
driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys('+7985899998787')
driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys('Москва')
driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys('Россия')
driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys('QA')
driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys('SkyPro')
driver.find_element(By.CSS_SELECTOR, '[type=submit]').click()

def test_zip_code_color():
    color_zip_code = driver.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property('Color')
    print(color_zip_code)
    assert color_zip_code == 'rgb(132, 32, 41)'
    
def test_other_element_color():    
    colors_other_elemnts = driver.find_elements(By.CSS_SELECTOR, '.alert:not(#zip-code)')
    color_list = list()
    for color_element in colors_other_elemnts:
        color_list.append(color_element.value_of_css_property('Color'))
    print(color_list)
    for color in color_list:
        assert color == 'rgb(15, 81, 50)'

