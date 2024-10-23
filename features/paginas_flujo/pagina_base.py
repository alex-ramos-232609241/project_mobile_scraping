from time import sleep
from features.consts import SPEED_EXECUTION_X_PROCESS

class Page:
    
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        sleep(SPEED_EXECUTION_X_PROCESS)
        return self.driver.find_element(by=locator[0], value=locator[1])

    def click_on_element(self, locator):
        sleep(SPEED_EXECUTION_X_PROCESS)
        element = self.driver.find_element(by=locator[0], value=locator[1])
        element.click()

    def input(self, text, locator):
        sleep(SPEED_EXECUTION_X_PROCESS)
        input_text = self.driver.find_element(by=locator[0], value=locator[1])
        input_text.send_keys(text)

    def hide_keyboard(self):
        sleep(SPEED_EXECUTION_X_PROCESS)
        self.driver.hide_keyboard()

    def get_value_text(self, locator):
        sleep(SPEED_EXECUTION_X_PROCESS)
        value_text = self.driver.find_element(by=locator[0], value=locator[1])
        return value_text.text

    def clean_value(self, locator):
        clean_text = self.driver.find_element(by=locator[0], value=locator[1])
        clean_text.clear()
        