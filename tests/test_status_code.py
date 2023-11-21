import requests
from PageObject.status_page import StatusPage
from tests.base_test import BaseTest
from utilities.test_data import TestData


class TestStatusCode(BaseTest):
    def test_check_that_status_code_equal_500(self):
        status_page = StatusPage(self.driver)
        status_page.open_page(TestData.broken_url)
        status_page.click_second_link_button()
        self.driver.implicitly_wait(5)
        responce = requests.get(TestData.status_code_link)
        assert responce.status_code == 500

