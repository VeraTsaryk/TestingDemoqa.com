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
        assert text_box_page.get_text_out_put_name == 'Name:Jon Doe'
        assert text_box_page.get_text_out_put_email == 'Email:name@example.com'
        assert text_box_page.get_text_out_put_current_address == 'Current Address :current address'
        assert text_box_page.get_text_out_put_permanent_address == 'Permananet Address :your address'
