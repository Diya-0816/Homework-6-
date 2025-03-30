import logging
from dotenv import load_dotenv
import os

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

user = os.getenv("USER_NAME")
password = os.getenv("PASSWORD")

logger.info("Application started.")
logger.info(f"Loaded user: {user}")
