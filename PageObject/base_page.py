from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from termcolor import colored
import time


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def find2(self, locator, timeout=10):
        """ Find element on the page. """

        element = None

        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except:
            print(colored('Element not found on the page!', 'red'))

        return element

    def click(self, locator):
        # self.find(*locator).click()
        element = self.wait_to_be_clickable(locator)
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(element, 1, 1). \
            pause(0).click(on_element=element).perform()
        # element.click()
        # self.driver.find_element(*locator).click()

    def set(self, locator, value):
        self.find(*locator).clear()
        self.find(*locator).send_keys(value)

    def get_text(self, locator):
        return self.find(*locator).text

    def get_title(self):
        return self.driver.title

    def is_displayed(self, locator):
        return self.wait_until_not_visible(locator).is_displayed()

    def open_page(self, url):
        return self.driver.get(url)

    def wait_until_not_visible(self, locator, timeout=10):

        element = None

        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except:
            print(colored('Element not visible!', 'red'))

        if element:
            js = ('return (!(arguments[0].offsetParent === null) && '
                  '!(window.getComputedStyle(arguments[0]) === "none") &&'
                  'arguments[0].offsetWidth > 0 && arguments[0].offsetHeight > 0'
                  ');')
            visibility = self.driver.execute_script(js, element)
            iteration = 0

            while not visibility and iteration < 10:
                time.sleep(0.5)

                iteration += 1

                visibility = self.driver.execute_script(js, element)
                print('Element {0} visibility: {1}'.format(locator, visibility))

        return element

    def wait_to_be_clickable(self, locator, timeout: float = 10, check_visibility=True):
        """ Wait until the element will be ready for click. """

        element = None

        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except:
            print(colored('Element not clickable!', 'red'))

        if check_visibility:
            self.wait_until_not_visible(locator)

        return element

    def delete_advertising(self):
        self.driver.execute_script("document.getElementById('fixedban').style.display = 'none';")

    def wait_alert_is_displayed(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

    def accept_alert(self):
        self.driver.switch_to.alert.accept()