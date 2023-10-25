from selenium.webdriver.common.by import By
from selenium import webdriver


def test_go_to_book_store():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.maximize_window()
    browser.get('https://demoqa.com/profile')
    browser.find_element(By.CSS_SELECTOR, '#notLoggin-label > a:nth-child(1)').click()
    user_name = browser.find_element(By.ID, 'userName')
    login = "Ola"
    user_name.send_keys(login)
    password = browser.find_element(By.ID, 'password')
    passwordName = '12345@Ola'
    password.send_keys(passwordName)
    login_button = browser.find_element(By.ID, 'login')
    login_button.click()
    button_go_to_store = browser.find_element(By.ID, 'gotoStore')
    button_go_to_store.click()
    book_store = browser.find_element(By.CLASS_NAME, 'main-header')
    assert book_store.is_displayed()
    assert book_store.text == 'Book Store'
