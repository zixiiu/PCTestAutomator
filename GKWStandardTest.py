from collections import deque

import Actions
import time
import datetime
import pyautogui as pg

import LoggerFormater
from TestStepUtils import loop_until, browser_url_loop_until, wait_until

import logging
import sys
import os

start_time = time.time()
### logging stuff

rootLogger = logging.getLogger()
rootLogger.setLevel(logging.INFO)
folder_name = datetime.datetime.now().strftime('test_%Y-%m-%d-%H-%M-%S')
os.mkdir(folder_name)
fileHandler = logging.FileHandler("{0}/{1}.log".format(folder_name, 'log'))
fileHandler.setFormatter(LoggerFormater.BTFormatter())
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler(sys.stdout)
consoleHandler.setFormatter(LoggerFormater.BTFormatter())
rootLogger.addHandler(consoleHandler)


### screenshot
def screenshot():
    pg.screenshot('%s/%dm%ds.jpg' % (folder_name, *divmod(time.time() - start_time, 60)))


### actual test start!
test_flag = False if len(sys.argv) == 1 else True
if sys.platform == 'win32':
    a = Actions.Windows.Windows()
elif sys.platform == 'darwin':
    a = Actions.Macintosh.Mac()
else:
    raise ValueError('what the hack is this computer?')

logging.info('Battery test started. %s Run.'% ('Test' if test_flag else 'Real'))
screenshot()

loop = 0
loop_start_m = 0
while True:
    logging.info('Loop %d started.' % loop)
    # Netease Music
    logging.info('Starting Netease Music.')
    a.launch_netease_music()

    # QQ login
    logging.info('Starting QQ.')
    a.launch_qq()

    # Excel
    logging.info('Starting MS Excel.')
    a.launch_ms_excel()
    loop_until(start_time, a.ms_excel_cal, test_flag, (loop_start_m + 10) * 60)
    screenshot()
    logging.info('End MS Excel.')
    # PPT
    logging.info('Starting MS PPT.')
    a.launch_ms_ppt()
    loop_until(start_time, a.ms_ppt_actions, test_flag, (loop_start_m + 20) * 60)
    screenshot()
    logging.info('End MS PPT.')
    # Word
    logging.info('Starting MS Word.')
    a.launch_ms_word()
    loop_until(start_time, a.type_and_remove, test_flag, (loop_start_m + 30) * 60)
    screenshot()
    logging.info('End MS Word.')

    # Browser
    logging.info('Start Browser.')
    urls = deque(
        ['jd.com', 'taobao.com', 'search:Geekerwan', 'sina.com.cn', '163.com', 'ithome.com',
         'https://www.chiphell.com/forum-314-1.html',
         'http://bbs.nga.cn/thread.php?fid=436&rand=211', 'gamersky.com', '3dmgame.com', '4399.com',
         'https://www.apple.com.cn/macbook-air-m2/', 'search:iPhone', 'search:Huawei', 'search:Xiaomi'])

    a.launch_browser()
    browser_url_loop_until(start_time, urls, a, test_flag, (loop_start_m + 40) * 60)
    screenshot()

    # browser video
    logging.info('Start Browser Video')
    a.browser_new_tab('https://www.bilibili.com/video/BV1Af4y1f7NJ')
    wait_until(start_time, test_flag, (loop_start_m + 50) * 60)
    screenshot()
    pg.press('space')  # pause the video
    logging.info('End Browser.')

    # IM
    logging.info('Start IM')
    a.qq_go_to_chat()
    loop_until(start_time, a.type_and_remove, test_flag, (loop_start_m + 60) * 60)
    logging.info('End IM')

    # Rebase!
    logging.info('Rebasing to original state...')
    a.quit_everything()


    # loop count!
    loop += 1
    loop_start_m += 60
