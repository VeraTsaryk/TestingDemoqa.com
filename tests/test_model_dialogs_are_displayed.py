from selenium.webdriver.common.by import By
from selenium import webdriver

from PageObject.dialogs_page import DialogsPage
from tests.base_test import BaseTest
from utilities.test_data import TestData


class TestDialogsAreDisplayed(BaseTest):

    def test_model_dialogs_are_displayed(self):
        dialogs_page = DialogsPage(self.driver)
        dialogs_page.open_page(TestData.dialogs_url)
        dialogs_page.click_small_model()
        modal_body = dialogs_page.find(By.CLASS_NAME, 'modal-title')
        assert modal_body.is_displayed()
        assert modal_body.text == 'Small Modal'

    def test_large_model_dialog_is_displayed(self):
        dialogs_page = DialogsPage(self.driver)
        dialogs_page.open_page(TestData.dialogs_url)
        dialogs_page.click_large_model()
        modal_title = dialogs_page.find(By.CLASS_NAME, 'modal-title')
        assert modal_title.is_displayed()
        assert modal_title.text == 'Large Modal'
