from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.book_locators import BookLocators
from PageObject.book_page import BookPage
from tests.base_test import BaseTest
from utilities.test_data import TestData


class TestBooks(BaseTest):
    def test_add_book_into_your_profile(self):
        page = BookPage(self.driver)
        page.open_page(TestData.book_url)
        page.click_book()
        page.click_login_form()
        page.log_into_application('Ola', '12345@Ola')
        page.click_add_to_collection_button()
        page.wait_alert_is_displayed()
        page.accept_alert()
        page.click_user_profile()
        assert page.book_is_displayed()

    def test_check_search_books(self):
        book_page = BookPage(self.driver)
        book_page.open_page(TestData.book_url)
        book_page.set_search_field('Git Pocket Guide')
        assert book_page.get_text(BookLocators.book) == 'Git Pocket Guide'
        book_page.set_search_field('Lud')
        book = book_page.find2(BookLocators.book, 2)
        assert book is None

    def test_go_to_book_store(self):
        book_page = BookPage(self.driver)
        book_page.open_page(TestData.profile_url)
        book_page.click_login_button_in_profile()
        book_page.log_into_application('Ola', '12345@Ola')
        book_page.delete_advertising()
        book_page.click_button_go_to_store()
        assert book_page.book_store_is_displayed()
        assert book_page.get_text(BookLocators.book_store) == 'Book Store'

    def test_delete_book_from_profile(self):
        book_page = BookPage(self.driver)
        book_page.open_page(TestData.book_url)
        book_page.click_book()
        book_page.click_login_form()
        book_page.log_into_application('Ola', '12345@Ola')
        book_page.click_add_to_collection_button()
        book_page.wait_alert_is_displayed()
        book_page.accept_alert()
        book_page.click_user_profile()
        assert book_page.book_is_displayed()
        book_page.click_delete_button()
        book_page.click_close_small_model()
        book_page.wait_alert_is_displayed()
        book_page.accept_alert()
        book = book_page.find2(BookLocators.book, 2)
        assert book is None
