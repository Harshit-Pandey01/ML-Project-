import sys
from src.mlproject.logger import logging


def error_message_detail(error, error_detail: sys):
    exc_type, exc_value, exc_tb = sys.exc_info()  # ✅ directly use sys

    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
    else:
        file_name = "Unknown"
        line_number = "Unknown"

    error_message = f"Error occurred in python script name [{file_name}] line number [{line_number}] error message [{str(error)}]"

    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message_detail(error_message, error_details)
        super().__init__(self.error_message)
        logging.error(self.error_message)

    def __str__(self):
        return self.error_message