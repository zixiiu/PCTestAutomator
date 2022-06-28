import Actions
import time

a = Actions.Windows.Windows()
# a.launch_browser()
# a.launch_ms_word()
# a.type_and_remove()
# time.sleep(1)
urls = ['jd.com', 'taobao.com', 'sina.com', '163.com', 'ithome.com', 'https://www.chiphell.com/forum-314-1.html',
        'http://bbs.nga.cn/thread.php?fid=436&rand=211', 'gamersky.com', '3dmgame.com', '4399.com',
        'https://www.apple.com.cn/macbook-air-m2/']

for idx, url in enumerate(urls):
        if idx == 0:
                a.launch_browser(url)
                a.browser_browse()
        else:
                a.browser_new_tab(url)
                a.browser_browse()
