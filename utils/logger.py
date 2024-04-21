import logging


def setup_logger(level: int = logging.INFO) -> None:
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        format="%(asctime)s %(levelname)s | %(name)s: %(message)s",
        datefmt="[%H:%M:%S]",
        level=level,
    )
    return logger
