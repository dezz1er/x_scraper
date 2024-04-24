import os

from dotenv import load_dotenv
from seleniumbase import Driver

from auth.login import LoginManager
from utils.logger import setup_logger
from utils.SBManager import SeleniumBaseManager

TWITTER_LOGIN_URL = "https://twitter.com/i/flow/login"
load_dotenv()


class XParsePost:
    def __init__(self, logger, url: str, sb: SeleniumBaseManager) -> None:
        self.logger = logger
        self.url = url
        self.driver: Driver = sb.driver

    def auth(self) -> None:
        username = os.getenv("USERNAME")
        password = os.getenv('PASSWORD')
        self.logger.info(f"Loggin with user:'{username}'")
        try:
            logging_service = LoginManager(
                self.driver, username, password
            )
            logging_service.x_login()
            self.logger.info(f'Logged into {username}')
        except Exception as e:
            self.logger.error(e)

    def parse_url(self) -> None:
        self.driver.open(url)
        self.driver.sleep(120)


if __name__ == "__main__":
    logger = setup_logger()
    url = "https://twitter.com/elonmusk"
    driver = SeleniumBaseManager()
    XParsePost(logger, url, driver).auth()
