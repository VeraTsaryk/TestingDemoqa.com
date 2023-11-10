from selenium.webdriver.common.by import By
from PageObject.age_page import AgePage
from tests.base_test import BaseTest
from utilities.test_data import TestData


class TestEditAge(BaseTest):
    def test_edit_user_age(self):
        age_page = AgePage(self.driver)
        age_page.open_page(TestData.web_tables_url)
        #edit_field_age = age_page.find(By.CSS_SELECTOR, '.rt-tbody > div:nth-child(1) .rt-td:nth-child(3)')
        assert age_page.get_text_field_age == '39'
        age_page.click_rename_button()
        age_page.set_age_field('59')
        age_page.click_submit_button()
        #edit_field_age = age_page.find(By.CSS_SELECTOR, '.rt-tbody > div:nth-child(1) .rt-td:nth-child(3)')
        assert age_page.get_text_field_age == '59'
