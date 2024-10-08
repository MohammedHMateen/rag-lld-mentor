import logging


class CustomFormatter(logging.Formatter):
    grey = '\x1b[38;21m'
    blue = '\x1b[38;5;39m'
    yellow = '\x1b[38;5;226m'
    red = '\x1b[38;5;196m'
    bold_red = '\x1b[31;1m'
    reset = '\x1b[0m'

    def __init__(self, fmt):
        super().__init__()
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: self.grey + self.fmt + self.reset,
            logging.INFO: self.yellow + self.fmt + self.reset,
            logging.WARNING: self.blue + self.fmt + self.reset,
            logging.ERROR: self.red + self.fmt + self.reset,
            logging.CRITICAL: self.bold_red + self.fmt + self.reset
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def get_logger():
    # Create custom logger logging all five levels
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Define format for logs
    fmt = '[%(asctime)s] | (thread: %(thread)d) | %(levelname)s | %(filename)s:%(lineno)2d | %(message)s'

    # Create stdout handler for logging to the console (logs all five levels)
    stdout_handler = logging.StreamHandler()
    stdout_handler.setLevel(logging.INFO)
    stdout_handler.setFormatter(CustomFormatter(fmt))

    # Create file handler for logging to a file (logs all five levels)
    # today = datetime.date.today()
    # file_handler = logging.FileHandler('my_app_{}.log'.format(today.strftime('%Y_%m_%d')))
    # file_handler.setLevel(logging.INFO)
    # file_handler.setFormatter(logging.Formatter(fmt))
    # yek_ipa_ianepo-sk-gHpDAUXbjzdy
    # 50kuX45wT3BlbkFJpj
    # 15S6yvMhNvl8AJGpcc
    # ym_yek_ipa_ianepo-sk-proj-XtQQE--gnxCzsut
    # 5wC5C9cLhFOanw7OnAi0snHS-6ReFtkJgv
    # 2OwjLgNGNkiePJN4sqLYzE3uIT3BlbkFJEqTYZH8t-qSyCyPGI-JD9lvxT
    # 18VFqxpfnrPE5ZLV6PidmWVKXS2VhAvJzIkTLuw9DsVGT0gYA

    # Add both handlers to the logger
    if not logger.hasHandlers():
        logger.addHandler(stdout_handler)
        # logger.addHandler(file_handler)

    return logger
