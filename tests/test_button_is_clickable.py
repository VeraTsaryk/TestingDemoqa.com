from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains

from PageObject.click_page import ClickPage
from tests.base_test import BaseTest
from utilities.test_data import TestData


class TestButtonIsClickable(BaseTest):
    def test_click_button(self):
        click_page = ClickPage(self.driver)
        click_page.open_page(TestData.buttons_url)
        click_page.click(ClickPage.button_dynamic_click)
        actual_message = click_page.find(By.ID, 'dynamicClickMessage')
        assert actual_message.is_displayed()

    def test_button_is_double_clickable(self):
        click_page = ClickPage(self.driver)
        click_page.open_page(TestData.buttons_url)
        click_page.double_click()
        actual_text_about_double_click = click_page.find(click_page.text_about_double_click)
        assert actual_text_about_double_click.is_displayed()

    def test_button_is_right_clickable(self):
        click_page = ClickPage(self.driver)
        click_page.open_page(TestData.buttons_url)
        click_page.right_click_button()
        actual_text_right_click = click_page.find(click_page.button_right_click)
        assert actual_text_right_click.is_displayed()

    def test_check_that_button_yes_is_clickable(self):
        click_page = ClickPage(self.driver)
        click_page.open_page(TestData.radio_buttons_url)
        click_page.click(click_page.yes_button)
        # to do Find and display function doesn't work
        answer = click_page.find(click_page.answer)
        assert answer.is_displayed()

    def test_check_that_button_impressive_is_clickable(self):
        click_page = ClickPage(self.driver)
        click_page.open_page(TestData.radio_buttons_url)
        click_page.click(click_page.impressive_button)
        # to do Find and display function doesn't work
        answer = click_page.find(click_page.answer)
        assert answer.is_displayed()

