from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


def test_add_book_into_your_profile():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
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
    WebDriverWait(browser, 10).until(EC.alert_is_present())
    browser.switch_to.alert.accept()
    user_profile = browser.find_element(By.CSS_SELECTOR, '.accordion :nth-child(6) > div > ul> li:nth-child(3)')
    action = ActionChains(browser)
    action.move_to_element(user_profile)
    action.perform()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.accordion :nth-child(6) > div > ul> li:nth-child(3)' )))
    user_profile.click()
    book = browser.find_element(By.ID, 'see-book-Git Pocket Guide')
    assert book.is_displayed()


def test_check_search_books():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get('https://demoqa.com/books')
    search_field = browser.find_element(By.ID, 'searchBox')
    book_name = 'Git Pocket Guide'
    search_field.send_keys(book_name)
    book = browser.find_element(By.ID, 'see-book-Git Pocket Guide')
    assert book.text == book_name
    search_field = browser.find_element(By.ID, 'searchBox')
    new_search = 'Lud'
    search_field.send_keys(new_search)
    assert book != True


def test_delete_book_from_profile():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
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
    WebDriverWait(browser, 10).until(EC.alert_is_present())
    browser.switch_to.alert.accept()
    user_profile = browser.find_element(By.CSS_SELECTOR, '.accordion :nth-child(6)>div>ul>li:nth-child(3)')
    # Why do css-selektor work sometimes?
    user_profile.click()
    book = browser.find_element(By.ID, 'see-book-Git Pocket Guide')
    assert book.is_displayed()
    delete_button = browser.find_element(By.ID, 'delete-record-undefined')
    delete_button.click()
    browser.find_element(By.ID, 'closeSmallModal-ok').click()
    WebDriverWait(browser, 10).until(EC.alert_is_present())
    browser.switch_to.alert.accept()
    assert book != True

