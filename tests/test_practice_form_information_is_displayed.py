from PageObject.practice_page import PracticePage
from tests.base_test import BaseTest
from utilities.test_data import TestData


class TestPracticeForm(BaseTest):
    def test_practice_form_information_is_displayed(self):
        practice_page = PracticePage(self.driver)
        practice_page.open_page(TestData.practice_form_url)
        practice_page.fill_practice_form_information(
            'Igor', 'Ivanov', 'igor@example.com', '6532489752'
        )
        practice_page.click_submit_button()
        assert practice_page.form_is_displayed()

