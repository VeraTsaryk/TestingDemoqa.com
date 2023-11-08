from selenium.webdriver.common.by import By
from selenium import webdriver

from PageObject.text_box_page import TextBoxPage
from tests.base_test import BaseTest
from utilities.test_data import TestData


class TestCreateUserTextBox(BaseTest):
    def test_create_new_user_text_box(self):
        text_box_page = TextBoxPage(self.driver)
        text_box_page.open_page(TestData.test_box_url)
        text_box_page.set_full_name('Jon Doe')
        text_box_page.set_email_name('name@example.com')
        text_box_page.set_current_address('current address')
        text_box_page.set_permanent_address('your address')
        text_box_page.click_submit_button()
        outputName = text_box_page.find(By.CSS_SELECTOR, '#output #name')
        assert outputName.text == 'Name:Jon Doe'
        outputEmail= text_box_page.find(By.CSS_SELECTOR, '#output #email')
        assert outputEmail.text == 'Email:name@example.com'
        outputCurrentAddress = text_box_page.find(By.CSS_SELECTOR, '#output #currentAddress')
        assert outputCurrentAddress.text == 'Current Address :current address'
        outputPermanentAddress = text_box_page.find(By.CSS_SELECTOR, '#output #permanentAddress')
        assert outputPermanentAddress.text == 'Permananet Address :your address'
