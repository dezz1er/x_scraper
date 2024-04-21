from dataclasses import dataclass
from seleniumbase import Driver


@dataclass
class LoginManager:
    driver: Driver
    username: str
    password: str

    def x_login(self):
        self.driver.type("//input[@autocomplete='username']", self.username)
        self.driver.click('span:contains("Далее")')
