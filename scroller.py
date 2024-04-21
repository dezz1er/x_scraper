class Scroller:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.current_position = 0
        self.last_position = driver
