import logging
import os

def setup_logger(report_path):
    log_file = os.path.join(report_path, "execution.log")

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger()
