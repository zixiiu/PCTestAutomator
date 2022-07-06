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
folder_name = datetime.datetime.now().strftime('test_%Y-%m-%d-%H:%M:%S')
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
test_flag = True
a = Actions.Macintosh.Mac()

logging.info('Battery test started.')
screenshot()

loop = 0
while True:
    loop += 1
    logging.info('Loop %d started.' % loop)
    # Netease Music
    a.launch_netease_music()

    # QQ login
    a.launch_qq()

    # Excel
    logging.info('Starting MS Excel.')
    a.launch_ms_excel()
    loop_until(start_time, a.ms_excel_cal, test_flag, 10 * 60)
    screenshot()
    logging.info('End MS Excel.')
    # PPT
    logging.info('Starting MS PPT.')
    a.launch_ms_ppt()
    loop_until(start_time, a.ms_ppt_actions, test_flag, 20 * 60)
    screenshot()
    logging.info('End MS PPT.')
    # Word
    logging.info('Starting MS Word.')
    a.launch_ms_word()
    loop_until(start_time, a.type_and_remove, test_flag, 30 * 60)
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
    browser_url_loop_until(start_time, urls, a, test_flag, 40 * 60)
    screenshot()

    # browser video
    logging.info('Start Browser Video')
    a.browser_new_tab('https://www.bilibili.com/video/BV1Af4y1f7NJ')
    wait_until(start_time, test_flag, 50 * 60)
    screenshot()
    pg.press('space')  # pause the video
    logging.info('End Browser.')

    # IM
    logging.info('Start IM')
    a.qq_go_to_chat()
    loop_until(start_time, a.type_and_remove, test_flag, 60 * 60)
    logging.info('End IM')

    # Rebase!
    logging.info('Rebasing to original state...')
    a.quit()  # qq
    a.quit()  # browser
    a.quit_no_save()  # word
    a.quit()  # ppt
    a.quit_no_save()  # excel
    a.quit()  # netease
