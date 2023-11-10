from selenium.webdriver.common.by import By
from PageObject.login_page import LoginPage
from tests.base_test import BaseTest
from utilities.test_data import TestData


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
        self.driver.implicitly_wait(2)
        actual_name = login_page.find(By.ID, 'userName-value')
        assert actual_name.is_displayed()
        assert actual_name.text == 'Ola'
        login_page.click_login_out_button()
        # Problem with find.element
        user_form = login_page.actual_form()
        assert actual_name != True
        assert user_form.is_displayed()
