import pytest
from selenium.webdriver.common.by import By
#from conftest import browser
from selenium import webdriver


def test_check_that_create_new_user():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get('https://demoqa.com/elements')
    text_box = browser.find_element(By.CLASS_NAME, 'text')
    text_box.click()
    full_name = browser.find_element(By.ID, 'userName')
    full_name.send_keys('user')
    email = browser.find_element(By.ID, 'userEmail')
    email.send_keys('name@example.com')
    current_address = browser.find_element(By.ID, 'currentAddress')
    current_address.send_keys('current address')
    permanent_address = browser.find_element(By.ID, 'permanentAddress')
    permanent_address.send_keys('your address')
    button_submit = browser.find_element(By.ID, 'submit')
    button_submit.click()
    result = browser.find_element(By.ID, 'output')
    #finish_text = ('Name:user \n'
     #              'Email:name@example.com \n'
      #             'Current Address:current address \n '
       #            'Permananet Address:your address ')
    assert result.is_displayed()

