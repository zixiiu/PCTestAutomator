import pyautogui as pg
import Actions.GenericActions
import time
import os


class Windows(Actions.GenericActions.GenericActions):

    def input_ent(self):
        pg.hotkey('ctrl', '0')
        time.sleep(1)

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
        time.sleep(1)
        self.input_ent()

    def launch_ms_ppt(self):
        self.launch_app_with_search('Powerpoint')
        pg.sleep(10)
        for _ in range(4):
            pg.press('tab')
            pg.sleep(0.5)
        pg.typewrite(['enter'])
        pg.sleep(1)

    def ms_ppt_actions(self):
        pg.press('f5')
        for i in range(5):
            pg.press('space')
        pg.press('escape')

    def launch_ms_excel(self):
        self.launch_app_with_search('Excel')
        pg.sleep(3)
        for _ in range(4):
            pg.press('tab')
            pg.sleep(0.5)
        pg.typewrite(['enter'])
        pg.sleep(1)
        self.input_ent()

    def ms_excel_cal(self):
        for i in ['B', 'E', 'H']:
            pg.typewrite('=SUM(%s2:%s15000)' % (i, i))
            pg.press('enter')

    def launch_qq(self):
        self.launch_app_with_search('TXQQ')
        time.sleep(20)
        self.input_ent()
        time.sleep(1)
        pg.typewrite('IM')
        time.sleep(1)
        pg.press('enter')

    def launch_netease_music(self):
        self.launch_app_with_search('wangyi')
        time.sleep(8)
        pg.hotkey('ctrl', 'p')
        time.sleep(1)

    def launch_browser(self):
        self.launch_app_with_search('Microsoft Edge')
        time.sleep(5)
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
        # pg.sleep(3)
        # pg.hotkey('ctrl', 'alt', 'z')
        pg.sleep(3)
        for _ in range(2):
            pg.hotkey('ctrl', 'alt', 'z')
            pg.sleep(3)
            self.input_ent()
            pg.sleep(3)
            pg.typewrite('IM')
            pg.sleep(3)
            pg.press('enter')
            pg.sleep(3)

    def quit(self):
        pg.hotkey('alt', 'f4')
        time.sleep(1)

    def quit_no_save(self):
        pg.hotkey('alt', 'f4')
        pg.sleep(10)
        pg.press('tab')
        pg.sleep(3)
        pg.press('n')
        pg.sleep(3)

    def quit_everything(self):
        # os.system('taskkill /f /im qq.exe')  # qq
        self.quit() # qq chat
        self.quit() # qq main
        self.quit() # browser
        self.quit_no_save()  # word
        self.quit() # ppt
        self.quit_no_save()  # excel
        # os.system('taskkill /im cloudmusic.exe') # netease music

