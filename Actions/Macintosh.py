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
        time.sleep(10)
        pg.press('return')

    def ms_ppt_actions(self):
        with pg.hold(['command', 'shift']):
            pg.press('return')
        for i in range(5):
            pg.press('space')
        pg.press('escape')

    def launch_ms_ppt(self):
        self.launch_app_with_search('Microsoft Powerpoint')
        time.sleep(10)
        pg.press('tab')
        pg.press('return')

    def type_and_remove(self):
        to_type = 'Microsoft Word is the best IDE on this planet! %s \n' % time.strftime('%Y-%m-%d %H:%M:%S')
        pg.typewrite(to_type, interval=0.1)
        # pg.typewrite(['backspace' for _ in range(len(to_type))], interval=0.1)

    def launch_ms_excel(self):
        self.launch_app_with_search('Microsoft Excel')
        time.sleep(10)
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

    def qq_go_to_chat(self):
        with pg.hold('option'):
            pg.press('o')
        pg.typewrite('IM')
        pg.press('enter')
        # pg.hotkey('option', 'o')

    def launch_netease_music(self):
        pg.press('command')
        pg.sleep(1)
        self.launch_app_with_search('neteasemusic')
        pg.sleep(2)
        pg.press('space')

    def quit(self):
        pg.hotkey('command', 'q')

    def quit_no_save(self):
        pg.hotkey('command', 'q')
        pg.hotkey('command', 'd')

    def quit_everything(self):
        self.quit()  # browser
        self.quit_no_save()  # word
        self.quit()  # ppt
        self.quit_no_save()  # excel
        # self.quit()  # netease












