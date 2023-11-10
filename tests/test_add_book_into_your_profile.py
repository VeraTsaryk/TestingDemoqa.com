from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObject.book_page import BookPage
from tests.base_test import BaseTest
from utilities.test_data import TestData


class TestBookApplication(BaseTest):
    def test_add_book_into_your_profile(self):
        book_page = BookPage(self.driver)
        book_page.open_page(TestData.book_url)
        book_page.click_book()
        book_page.click_login_form()
        book_page.log_into_application('Ola', '12345@Ola')
        self.driver.implicitly_wait(5)
        book_page.click_add_to_collection_button()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()
        book_page.click_user_profile()
        book = book_page.find(By.ID, 'see-book-Git Pocket Guide')
        # to do Find and display function doesn't work
        assert book.is_displayed()

    def test_check_search_books(self):
        book_page = BookPage(self.driver)
        book_page.open_page(TestData.book_url)
        book_page.set_search_field('Git Pocket Guide')
        # to do Find function doesn't work in PageObject
        book = book_page.find(By.ID, 'see-book-Git Pocket Guide')
        assert book.text == 'Git Pocket Guide'
        book_page.set_search_field('Lud')
        assert book != True

    def test_go_to_book_store(self):
        book_page = BookPage(self.driver)
        book_page.open_page(TestData.profile_url)
        book_page.click_login_button_in_profile()
        book_page.log_into_application('Ola', '12345@Ola')
        self.driver.execute_script("window.scrollTo(0, 0)")
        self.driver.implicitly_wait(5)
        book_page.click_button_go_to_store()
        # to do Find and display function doesn't work
        book_store = book_page.find(By.CLASS_NAME, 'main-header')
        assert book_store.is_displayed()
        assert book_store.text == 'Book Store'

    def test_delete_book_from_profile(self):
        book_page = BookPage(self.driver)
        book_page.open_page(TestData.book_url)
        book_page.click_book()
        book_page.click_login_form()
        book_page.log_into_application('Ola', '12345@Ola')
        self.driver.implicitly_wait(5)
        book_page.click_add_to_collection_button()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()
        book_page.click_user_profile()
        # to do Find and display function doesn't work
        book = book_page.find(By.ID, 'see-book-Git Pocket Guide')
        assert book.is_displayed()
        book_page.click_delete_button()
        book_page.click_close_small_model()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()
        assert book != True







# def test_add_book_into_your_profile():
#     browser = webdriver.Chrome()
#     browser.implicitly_wait(5)
#     browser.maximize_window()
#     browser.get('https://demoqa.com/books')
#     book = browser.find_element(By.ID, 'see-book-Git Pocket Guide')
#     book.click()
#     login_button = browser.find_element(By.ID, 'login')
#     login_button.click()
#     user_name = browser.find_element(By.ID, 'userName')
#     login = "Ola"
#     user_name.send_keys(login)
#     password = browser.find_element(By.ID, 'password')
#     passwordName = '12345@Ola'
#     password.send_keys(passwordName)
#     login_button = browser.find_element(By.ID, 'login')
#     login_button.click()
#     add_to_collection_button = browser.find_element(By.CSS_SELECTOR,
#                                                     'div[class = "text-right fullButton"] #addNewRecordButton')
#     add_to_collection_button.click()
#     WebDriverWait(browser, 10).until(EC.alert_is_present())
#     browser.switch_to.alert.accept()
#     user_profile = browser.find_element(By.CSS_SELECTOR, '.accordion :nth-child(6) > div > ul> li:nth-child(3)')
#     browser.execute_script("arguments[0].scrollIntoView()", user_profile)
#     user_profile.click()
#     book = browser.find_element(By.ID, 'see-book-Git Pocket Guide')
#     assert book.is_displayed()
#
#
# def test_check_search_books():
#     browser = webdriver.Chrome()
#     browser.implicitly_wait(5)
#     browser.get('https://demoqa.com/books')
#     search_field = browser.find_element(By.ID, 'searchBox')
#     book_name = 'Git Pocket Guide'
#     search_field.send_keys(book_name)
#     book = browser.find_element(By.ID, 'see-book-Git Pocket Guide')
#     assert book.text == book_name
#     search_field = browser.find_element(By.ID, 'searchBox')
#     new_search = 'Lud'
#     search_field.send_keys(new_search)
#     assert book != True
#
#
# def test_delete_book_from_profile():
#     browser = webdriver.Chrome()
#     browser.implicitly_wait(5)
#     browser.maximize_window()
#     browser.get('https://demoqa.com/books')
#     book = browser.find_element(By.ID, 'see-book-Git Pocket Guide')
#     book.click()
#     login_button = browser.find_element(By.ID, 'login')
#     login_button.click()
#     user_name = browser.find_element(By.ID, 'userName')
#     login = "Ola"
#     user_name.send_keys(login)
#     password = browser.find_element(By.ID, 'password')
#     passwordName = '12345@Ola'
#     password.send_keys(passwordName)
#     login_button = browser.find_element(By.ID, 'login')
#     login_button.click()
#     add_to_collection_button = browser.find_element(By.CSS_SELECTOR,
#                                                     'div[class = "text-right fullButton"] #addNewRecordButton')
#     add_to_collection_button.click()
#     WebDriverWait(browser, 10).until(EC.alert_is_present())
#     browser.switch_to.alert.accept()
#     user_profile = browser.find_element(By.CSS_SELECTOR, '.accordion :nth-child(6)>div>ul>li:nth-child(3)')
#     # Why do css-selektor work sometimes?
#     user_profile.click()
#     book = browser.find_element(By.ID, 'see-book-Git Pocket Guide')
#     assert book.is_displayed()
#     delete_button = browser.find_element(By.ID, 'delete-record-undefined')
#     delete_button.click()
#     browser.find_element(By.ID, 'closeSmallModal-ok').click()
#     WebDriverWait(browser, 10).until(EC.alert_is_present())
#     browser.switch_to.alert.accept()
#     assert book != True
#
#
# def test_go_to_book_store():
#     browser = webdriver.Chrome()
#     browser.implicitly_wait(5)
#     browser.maximize_window()
#     browser.get('https://demoqa.com/profile')
#     browser.find_element(By.CSS_SELECTOR, '#notLoggin-label > a:nth-child(1)').click()
#     user_name = browser.find_element(By.ID, 'userName')
#     login = "Ola"
#     user_name.send_keys(login)
#     password = browser.find_element(By.ID, 'password')
#     passwordName = '12345@Ola'
#     password.send_keys(passwordName)
#     login_button = browser.find_element(By.ID, 'login')
#     login_button.click()
#     button_go_to_store = browser.find_element(By.ID, 'gotoStore')
#     button_go_to_store.click()
#     book_store = browser.find_element(By.CLASS_NAME, 'main-header')
#     assert book_store.is_displayed()
#     assert book_store.text == 'Book Store'
