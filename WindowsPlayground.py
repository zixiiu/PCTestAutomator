from collections import deque

import Actions
import time

from TestStepUtils import browser_url_loop_until

a = Actions.Windows.Windows()

# a.launch_ms_ppt()
# a.ms_ppt_actions()
# a.ms_ppt_actions()

# a.launch_ms_excel()
# a.ms_excel_cal()
# a.ms_excel_cal()


# urls = deque(
#     ['jd.com', 'taobao.com', 'search:Geekerwan', 'sina.com.cn', '163.com', 'ithome.com',
#      'https://www.chiphell.com/forum-314-1.html',
#      'http://bbs.nga.cn/thread.php?fid=436&rand=211', 'gamersky.com', '3dmgame.com', '4399.com',
#      'https://www.apple.com.cn/macbook-air-m2/', 'search:iPhone', 'search:Huawei', 'search:Xiaomi'])
#
# a.launch_browser()
# browser_url_loop_until(0, urls, a, True, time.time() + 10000 )

a.qq_go_to_chat()