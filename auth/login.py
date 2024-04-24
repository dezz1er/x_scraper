from dataclasses import dataclass
from seleniumbase import Driver
from utils.locator import XLocator


@dataclass
class LoginManager:
    driver: Driver
    username: str
    password: str
    login_url: str = "https://twitter.com/i/flow/login"

    def x_login(self):
        self.driver.switch_to.new_window('tab')
        self.driver.open(self.login_url)
        self.driver.type(XLocator.LOG_USERNAME, self.username)
        self.driver.click(XLocator.LOG_BTN_NXT)
        self.driver.type(XLocator.LOG_PASSWORD, self.password)
        self.driver.click(XLocator.LOG_BTN_LOGIN)
        self.driver.sleep(10)
        self.driver.close()
