from loguru import logger
import sys

logger.remove()
logger.add(sys.stderr, level="INFO")

logger.add("app.log", rotation="10 MB", retention="10 days", level="ERROR")