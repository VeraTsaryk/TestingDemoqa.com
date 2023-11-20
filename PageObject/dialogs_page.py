from PageObject.base_page import BasePage
from Locators.dialogs_locators import DialogsLocators


class DialogsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_small_model(self):
        self.click(DialogsLocators.small_model)

    def click_large_model(self):
        self.click(DialogsLocators.large_model)

    @property
    def get_text_modal_title(self):
        return self.get_text(DialogsLocators.modal_title)

    def modal_is_displayed(self):
        return self.is_displayed(DialogsLocators.modal_title)
