import time
import datetime
import logging
import psutil


class BTFormatter(logging.Formatter):

    def __init__(self):
        super().__init__()
        self.start_time = time.time()

    def format(self, record):
        elapsed_seconds = record.created - self.start_time
        times = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        deltam, deltas = divmod(elapsed_seconds, 60)
        battery = psutil.sensors_battery()
        percent = str(battery.percent)
        return "%s : %dm%ds : %s : %s : %s" % (times, deltam, deltas, percent, record.levelname, record.getMessage())
