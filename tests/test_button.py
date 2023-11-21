from PageObject.click_page import ClickPage
from tests.base_test import BaseTest
from utilities.test_data import TestData
from Locators.click_locators import ClickLocators


class TestButton(BaseTest):
    def test_click_button(self):
        click_page = ClickPage(self.driver)
        click_page.open_page(TestData.buttons_url)
        click_page.click(ClickLocators.button_dynamic_click)
        assert click_page.actual_message_is_displayed()

    def test_button_is_double_clickable(self):
        click_page = ClickPage(self.driver)
        click_page.open_page(TestData.buttons_url)
        click_page.double_click()
        assert click_page.actual_text_about_double_click_is_displayed()

    def test_button_is_right_clickable(self):
        click_page = ClickPage(self.driver)
        click_page.open_page(TestData.buttons_url)
        click_page.right_click_button()
        assert click_page.actual_text_about_right_click_is_displayed()

    def test_check_that_button_yes_is_clickable(self):
        click_page = ClickPage(self.driver)
        click_page.open_page(TestData.radio_buttons_url)
        click_page.click(ClickLocators.yes_button)
        assert click_page.answer_is_displayed()

    def test_check_that_button_impressive_is_clickable(self):
        click_page = ClickPage(self.driver)
        click_page.open_page(TestData.radio_buttons_url)
        click_page.click(ClickLocators.impressive_button)
        assert click_page.answer_is_displayed()
