from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver


def test_new_user_error():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get('https://demoqa.com/login')
    new_user_button = browser.find_element(By.ID, 'newUser')
    new_user_button.click()
    first_name = browser.find_element(By.ID, 'firstname')
    first_name.send_keys('Fill')
    last_name = browser.find_element(By.ID, 'lastname')
    last_name.send_keys('Jons')
    user_name = browser.find_element(By.ID, 'userName')
    user_name.send_keys('Filly')
    password = browser.find_element(By.ID, 'password')
    password.send_keys('123456')
    robot_button = browser.find_element(By.CLASS_NAME, 'recaptcha-checkbox-border')
    browser.execute_script("arguments[0].checked = true;", robot_button)
    register_button = browser.find_element(By.ID, 'register')
    register_button.click()
    password_error = browser.find_element(By.CLASS_NAME, 'mb-1')
    error_text = 'Passwords must have at least one non alphanumeric character, one digit ("0"-"9"), one uppercase ("A"-"Z"), one lowercase ("a"-"z"), one special character and Password must be eight characters or longer.'
    assert password_error.text == error_text
