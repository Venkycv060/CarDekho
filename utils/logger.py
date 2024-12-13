# The logger.py will handle logging, so you can track events, errors, and test progress throughout the automation process.

import logging
import os


class Logger:
    def __init__(self, log_file='test_automation.log'):
        self.log_file = log_file
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        # Create a file handler to save logs to a file
        if not os.path.exists('logs'):
            os.makedirs('logs')

        log_path = os.path.join('logs', self.log_file)
        file_handler = logging.FileHandler(log_path)
        file_handler.setLevel(logging.INFO)

        # Create a stream handler to print logs to console
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)

        # Create log format
        log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(log_format)
        stream_handler.setFormatter(log_format)

        # Add handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)

    def info(self, message):
        """Log an info message."""
        self.logger.info(message)

    def debug(self, message):
        """Log a debug message."""
        self.logger.debug(message)

    def error(self, message):
        """Log an error message."""
        self.logger.error(message)

    def warning(self, message):
        """Log a warning message."""
        self.logger.warning(message)

    def critical(self, message):
        """Log a critical error message."""
        self.logger.critical(message)
