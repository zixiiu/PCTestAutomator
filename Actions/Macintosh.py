import pyautogui as pg
import Actions.GenericActions
import time


class Mac(Actions.GenericActions.GenericActions):
    def launch_app_with_search(self, kw):
        with pg.hold('command'):
            pg.press('space')
        pg.typewrite(kw, interval=0.05)
        pg.press('return')

    def launch_ms_word(self):
        self.launch_app_with_search('Microsoft Word')
        time.sleep(1)
        pg.press('return')

    def ms_ppt_actions(self):
        with pg.hold(['command', 'shift']):
            pg.press('return')
        for i in range(5):
            pg.press('space')
        pg.press('escape')

    def launch_ms_ppt(self):
        self.launch_app_with_search('Microsoft Powerpoint')
        time.sleep(1)
        pg.press('tab')
        pg.press('return')

    def type_and_remove(self):
        to_type = 'Microsoft Word is the best IDE on this planet! \n'
        pg.typewrite(to_type, interval=0.1)
        # pg.typewrite(['backspace' for _ in range(len(to_type))], interval=0.1)

    def launch_ms_excel(self):
        self.launch_app_with_search('Microsoft Excel')
        time.sleep(1)
        pg.press('tab')
        pg.press('return')



    def ms_excel_cal(self):
        for i in ['B', 'E', 'H']:
            # with pg.hold('control'):
            #     pg.press('u')

            pg.typewrite('=SUM(%s2:%s15000)' % (i, i))
            pg.press('return')

    def launch_browser(self):
        self.launch_app_with_search('Safari')
        # pg.hotkey('command', 'l')
        # pg.typewrite(url, interval=0.05)
        # pg.press('return')

    def browser_new_tab(self, url):
        pg.hotkey('command', 't')
        pg.typewrite(url, interval=0.05)
        pg.typewrite(['return'])

    def browser_browse(self):
        pg.sleep(5)
        for _ in range(5):
            pg.press('space')
            pg.sleep(3)

    def browser_search(self, kw):
        self.browser_new_tab('baidu.com')
        pg.typewrite(kw, interval=0.1)
        pg.press('return')

    def launch_qq(self):
        self.launch_app_with_search('qq')

    def launch_netease_music(self):
        self.launch_app_with_search('neteasemusic')
        pg.sleep(2)
        pg.press('space')







