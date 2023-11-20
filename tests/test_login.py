from PageObject.login_page import LoginPage
from tests.base_test import BaseTest
from utilities.test_data import TestData
from Locators.login_locators import LoginLocators


class TestLogin(BaseTest):
    def test_book_store_application_login_invalid_user(self):
        self.driver.get(TestData.url)
        login_page = LoginPage(self.driver)
        login_page.log_into_application("Verlo", "1234lol")
        self.driver.implicitly_wait(2)
        actual_message = login_page.get_warning_message()
        assert actual_message.__contains__("Invalid username or password!")

    def test_book_store_application_login_ok(self):
        login_page = LoginPage(self.driver)
        login_page.open_page(TestData.url)
        login_page.log_into_application(TestData.email, TestData.password)
        actual_title = login_page.get_title()
        assert actual_title == 'DEMOQA'

    def test_log_out(self):
        login_page = LoginPage(self.driver)
        login_page.open_page(TestData.url)
        login_page.log_into_application(TestData.email, TestData.password)
        assert login_page.actual_name_is_displayed()
        assert login_page.get_text_actual_name == 'Ola'
        login_page.click_login_out_button()
        actual_name = login_page.find2(LoginLocators.actual_name, 2)
        assert actual_name is None
        assert login_page.user_form_is_displayed()
