import logging
import os
from datetime import datetime

# Create a unique log file name using current date & time
# Example: 02_22_2026_14_30_10.log
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create full path: current_working_directory/logs/<log_file_name>
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create the directory if it doesn't exist
# exist_ok=True prevents error if folder already exists
os.makedirs(log_path, exist_ok=True)

# Final log file path where logs will be stored
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# Configure logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,  # File where logs will be written
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Log format
    level=logging.INFO,  # Minimum logging level (INFO and above)
) 

 