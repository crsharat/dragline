from dragline.settings import Settings
import logging

settings = Settings()
request_processor = None
logger = logging.getLogger('dragline')
spider = None
stats = dict()
