import logging
import os

class Logger:

    def __init__(self, report_path):
        log_file = os.path.join(report_path, "execution.log")

        self.logger = logging.getLogger("AutomationLogger")
        self.logger.setLevel(logging.INFO)

        # Duplicate logs se bachne ke liye
        if not self.logger.handlers:
            file_handler = logging.FileHandler(log_file)
            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger
