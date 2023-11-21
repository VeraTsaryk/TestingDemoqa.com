from PageObject.dialogs_page import DialogsPage
from tests.base_test import BaseTest
from utilities.test_data import TestData


class TestDialogs(BaseTest):

    def test_model_dialogs_are_displayed(self):
        dialogs_page = DialogsPage(self.driver)
        dialogs_page.open_page(TestData.dialogs_url)
        dialogs_page.click_small_model()
        assert dialogs_page.modal_is_displayed()
        assert dialogs_page.get_text_modal_title == 'Small Modal'

    def test_large_model_dialog_is_displayed(self):
        dialogs_page = DialogsPage(self.driver)
        dialogs_page.open_page(TestData.dialogs_url)
        dialogs_page.click_large_model()
        assert dialogs_page.modal_is_displayed()
        assert dialogs_page.get_text_modal_title == 'Large Modal'
