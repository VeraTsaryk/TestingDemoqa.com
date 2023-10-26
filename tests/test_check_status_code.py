import pytest
from selenium.webdriver.common.by import By
import requests
#from conftest import browser
from selenium import webdriver


def test_check_that_create_new_user():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get('https://demoqa.com/broken')
    second_link_button = browser.find_element(By.CSS_SELECTOR, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div:nth-child(2) > a:nth-child(14)')
    second_link_button.click()
    browser.implicitly_wait(5)
    responce = requests.get('https://the-internet.herokuapp.com/status_codes/500')
    assert responce.status_code == 500
