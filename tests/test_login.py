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

# def test_book_store_application_login_ok(browser):
#     browser.get('https://demoqa.com/login')
#     user_name = browser.find_element(By.ID, 'userName')
#     login = "Ola"
#     user_name.send_keys(login)
#     password = browser.find_element(By.ID, 'password')
#     passwordName = '12345@Ola'
#     password.send_keys(passwordName)
#     new_user_button = browser.find_element(By.ID, 'login')
#     new_user_button.click()
#     browser.get('https://demoqa.com/profile')
#     profile = browser.find_element(By.CLASS_NAME, 'main-header')
#     assert profile.text == 'Profile'
#
#
# def test_log_out(browser):
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
#     profile_name = browser.find_element(By.ID, 'userName-value')
#     assert profile_name.is_displayed()
#     assert profile_name.text == 'Ola'
#     log_out_button = browser.find_element(By.CSS_SELECTOR, 'div[class = "text-right col-md-5 col-sm-12"] #submit')
#     log_out_button.click()
#     user_form = browser.find_element(By.CSS_SELECTOR, '#userForm > div:nth-child(1)')
#     assert profile_name != True
#     assert user_form.is_displayed()
