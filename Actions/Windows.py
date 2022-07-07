import pyautogui as pg
import Actions.GenericActions
import time


class Windows(Actions.GenericActions.GenericActions):

    def input_ent(self):
        pg.hotkey('ctrl', '0')

    def launch_app_with_search(self, kw):
        pg.typewrite(['win'])
        pg.typewrite(kw, interval=0.05)
        pg.typewrite(['enter'])

    def type_and_remove(self):
        to_type = 'Microsoft Word is the best IDE on this planet! %s \n' % time.strftime('%Y-%m-%d %H:%M:%S')
        pg.typewrite(to_type, interval=0.1)

    def launch_ms_word(self):
        self.launch_app_with_search('Word')
        time.sleep(10)
        pg.typewrite(['enter'])
        self.input_ent()

    def launch_ms_ppt(self):
        self.launch_app_with_search('Powerpoint')
        pg.sleep(10)
        for _ in range(4):
            pg.press('tab')
        pg.typewrite(['enter'])
        pg.sleep(1)

    def ms_ppt_actions(self):
        pg.press('f5')
        for i in range(5):
            pg.press('space')
        pg.press('escape')

    def launch_ms_excel(self):
        self.launch_app_with_search('Microsoft Excel')
        pg.sleep(3)
        for _ in range(4):
            pg.press('tab')
        pg.typewrite(['enter'])
        pg.sleep(1)
        self.input_ent()

    def ms_excel_cal(self):
        for i in ['B', 'E', 'H']:
            pg.typewrite('=SUM(%s2:%s15000)' % (i, i))
            pg.press('enter')

    def launch_qq(self):
        self.launch_app_with_search('QQ')
        time.sleep(10)
        pg.typewrite('IM')
        pg.press('enter')


    def launch_netease_music(self):
        self.launch_app_with_search('wangyi')
        time.sleep(8)
        pg.hotkey('ctrl', 'p')

    def launch_browser(self):
        self.launch_app_with_search('Microsoft Edge')
        # pg.hotkey('ctrl', 'l')
        # pg.typewrite(url, interval=0.05)
        # pg.typewrite(['enter'])

    def browser_new_tab(self, url):
        pg.hotkey('ctrl', 't')
        self.input_ent()
        pg.typewrite(url, interval=0.05)
        pg.typewrite(['enter'])

    def browser_browse(self):
        # pg.typewrite(['tab' for _ in range(5)], interval=0.05)
        pg.sleep(5)
        for _ in range(5):
            pg.press('space')
            pg.sleep(3)

    def browser_search(self, kw):
        self.browser_new_tab('baidu.com')
        pg.sleep(1)
        pg.typewrite(kw, interval=0.1)
        pg.press('enter')

    def qq_go_to_chat(self):
        pg.hotkey('ctrl', 'alt', 'z')
        pg.hotkey('ctrl', 'alt', 'z')
        pg.sleep(1)
        self.input_ent()
        pg.typewrite('IM')
        pg.press('enter')

    def quit(self):
        pg.hotkey('alt', 'f4')

    def quit_no_save(self):
        pg.hotkey('alt', 'f4')
        pg.press('tab')
        pg.press('n')


