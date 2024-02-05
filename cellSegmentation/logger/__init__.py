import logging
import os
from datetime import datetime
from from_root import from_root

# Create the log directory path
log_dir = os.path.join(from_root(), 'log')

# Create the log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create the directory if it does not exist
os.makedirs(log_dir, exist_ok=True)

# Set the logging configuration
logging.basicConfig(
    filename=os.path.join(log_dir, LOG_FILE),
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Test logging
logging.info("Custom logging message")
