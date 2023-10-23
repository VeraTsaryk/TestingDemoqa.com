from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.alert import Alert


def test_add_book_into_your_profile ():
    #options = ChromeOptions()
    #options.add_argument("--start-maximized")

    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    #browser.get('https://demoqa.com/login')
    browser.maximize_window()
    browser.get('https://demoqa.com/books')
    book = browser.find_element(By.ID, 'see-book-Git Pocket Guide')
    book.click()
    login_button = browser.find_element(By.ID, 'login')
    login_button.click()
    user_name = browser.find_element(By.ID, 'userName')
    login = "Ola"
    user_name.send_keys(login)
    password = browser.find_element(By.ID, 'password')
    passwordName = '12345@Ola'
    password.send_keys(passwordName)
    login_button = browser.find_element(By.ID, 'login')
    login_button.click()
    add_to_collection_button = browser.find_element(By.CSS_SELECTOR, 'div[class = "text-right fullButton"] #addNewRecordButton')
    add_to_collection_button.click()
    # How do alert ?
    #WebDriverWait(driver, 10).until(EC.alert_is_present())
    browser.switch_to.alert.accept()
    #alert = browser.switch_to_alert()
    #alert_text = alert.text
    #alert.accept()
    assert True == True


