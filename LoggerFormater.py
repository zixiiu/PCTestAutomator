import time
import datetime
import logging


class BTFormatter(logging.Formatter):

    def __init__(self):
        super().__init__()
        self.start_time = time.time()

    def format(self, record):
        elapsed_seconds = record.created - self.start_time
        times = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        deltam, deltas = divmod(elapsed_seconds, 60)
        return "%s : %dm%ds : %s : %s" % (times, deltam, deltas, record.levelname, record.getMessage())

