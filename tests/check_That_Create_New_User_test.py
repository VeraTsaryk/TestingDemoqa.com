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
    username = 'Jon Doe'
    full_name.send_keys(username)
    email = browser.find_element(By.ID, 'userEmail')
    emailName = 'name@example.com'
    email.send_keys(emailName)
    current_address = browser.find_element(By.ID, 'currentAddress')
    current_address_name = 'current address'
    current_address.send_keys(current_address_name)
    permanent_address = browser.find_element(By.ID, 'permanentAddress')
    permanent_address_name = 'your address'
    permanent_address.send_keys(permanent_address_name)
    button_submit = browser.find_element(By.ID, 'submit')
    button_submit.click()
    outputName = browser.find_element(By.CSS_SELECTOR, '#output #name')
    assert outputName.text == f'Name:{username}'
    outputEmail= browser.find_element(By.CSS_SELECTOR, '#output #email')
    assert outputEmail.text == f'Email:{emailName}'
    outputCurrentAddress = browser.find_element(By.CSS_SELECTOR, '#output #currentAddress')
    assert outputCurrentAddress.text == f'Current Address :{current_address_name}'
    outputPermanentAddress = browser.find_element(By.CSS_SELECTOR, '#output #permanentAddress')
    assert outputPermanentAddress.text == f'Permananet Address :{permanent_address_name}'


    # TODO: check each property
    #finish_text = ('Name:user \n'
     #              'Email:name@example.com \n'
      #             'Current Address:current address \n '
       #            'Permananet Address:your address ')
    #assert result.is_displayed()

