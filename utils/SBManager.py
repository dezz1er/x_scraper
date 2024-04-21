from seleniumbase import Driver


class SeleniumBaseManager:
    def __init__(self, headless=False, use_chrome=True):
        """Initialize the SeleniumBaseManager with driver options."""
        self.driver = Driver(headless=headless, uc=use_chrome)
