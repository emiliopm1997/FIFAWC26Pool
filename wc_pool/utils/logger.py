from pathlib import Path
import logging
from typing import Optional


class Logger:
    """
    Singleton logger class for the application.

    This logger is configured to:
    - Log messages to both console and file
    - Use append mode for log file persistence
    - Include filename and line number in log format
    """

    _instance = None
    _logger: Optional[logging.Logger] = None

    def __new__(cls) -> logging.Logger:
        """
        Ensure only one instance of the Logger exists.

        Returns
        -------
        Logger
            Singleton instance of the Logger class.
        """
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._initialize_logger()
        return cls._instance

    def _initialize_logger(self):
        """
        Initialize the logger configuration.

        This sets up:
        - File handler (append mode)
        - Stream handler (console output)
        - Logging format including filename and line number
        """
        if self._logger is None:
            return  # Prevent re-initialization

        # Create logs directory using pathlib
        log_dir = Path.cwd() / "logs"
        log_dir.mkdir(exist_ok=True)

        log_file = log_dir / "wc_pool_logger.log"

        self._logger = logging.getLogger("wc_pool_logger")
        self._logger.setLevel(logging.INFO)

        # Prevent duplicate handlers
        if not self._logger.handlers:

            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
            )

            # File handler (append mode by default)
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.INFO)
            file_handler.setFormatter(formatter)

            # Console handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            console_handler.setFormatter(formatter)

            self._logger.addHandler(file_handler)
            self._logger.addHandler(console_handler)

    def get_logger(self) -> logging.Logger:
        """
        Retrieve the configured logger instance.

        Returns
        -------
        logging.Logger
            Configured logger instance.
        """
        if self._logger is None:
            raise RuntimeError("Logger has not been initialized")
        return self._logger
