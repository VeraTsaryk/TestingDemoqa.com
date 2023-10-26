from selenium.webdriver.common.by import By
from selenium import webdriver


def test_book_store_application_login_invalid_user():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get('https://demoqa.com/login')
    user_name = browser.find_element(By.ID, 'userName')
    user_name.send_keys('name@form.com')
    password = browser.find_element(By.ID, 'password')
    password.send_keys('658kod')
    new_user_button = browser.find_element(By.ID, 'login')
    new_user_button.click()
    invalid_name_error = browser.find_element(By.CLASS_NAME, 'mb-1')
    assert invalid_name_error.text == 'Invalid username or password!'


def test_book_store_application_login_ok():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get('https://demoqa.com/login')
    user_name = browser.find_element(By.ID, 'userName')
    login = "Ola"
    user_name.send_keys(login)
    password = browser.find_element(By.ID, 'password')
    passwordName = '12345@Ola'
    password.send_keys(passwordName)
    new_user_button = browser.find_element(By.ID, 'login')
    new_user_button.click()
    browser.get('https://demoqa.com/profile')
    profile = browser.find_element(By.CLASS_NAME, 'main-header')
    assert profile.text == 'Profile'

