from seleniumbase import SB
from utils.logger import setup_logger


class XParsePost:
    def __init__(self, logger, url) -> None:
        self.logger = logger
        self.url = url

    def parse(self) -> None:
        with SB(uc=True,
                ) as sb:
            try:
                self._get_page(self.url, sb)
            except Exception as error:
                self.logger.error(f'Ошибка: {error}')

    def _get_page(self, url, sb) -> str:
        sb.open(url)
        sb.sleep(15)


if __name__ == "__main__":
    logger = setup_logger()
    url = 'https://twitter.com/elonmusk'
    XParsePost(logger, url).parse()
