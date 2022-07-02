import pyautogui as pg
import Actions.GenericActions
import time


class Windows(Actions.GenericActions.GenericActions):

    def launch_app_with_search(self, kw):
        pg.typewrite(['win'])
        pg.typewrite(kw, interval=0.05)
        pg.typewrite(['enter'])

    def type_and_remove(self):
        to_type = 'Geekerwan 1m sub!'
        pg.typewrite(to_type, interval=0.1)
        pg.typewrite(['backspace' for _ in range(len(to_type))], interval=0.1)

    def launch_ms_word(self):
        self.launch_app_with_search('Microsoft Word')
        time.sleep(1)
        pg.typewrite(['enter'])

    def launch_ms_ppt(self):
        self.launch_app_with_search('Microsoft Powerpoint')
        time.sleep(1)
        pg.typewrite(['enter'])

    def launch_ms_excel(self):
        self.launch_app_with_search('Microsoft Excel')
        time.sleep(1)
        pg.typewrite(['enter'])

    def launch_qq(self):
        self.launch_app_with_search('QQ')
        time.sleep(1)

    def play_netease_music(self):
        self.launch_app_with_search('wangyi')
        time.sleep(5)
        pg.hotkey('ctrl', 'p')

    def launch_browser(self):
        self.launch_app_with_search('Microsoft Edge')
        # pg.hotkey('ctrl', 'l')
        # pg.typewrite(url, interval=0.05)
        # pg.typewrite(['enter'])

    def browser_new_tab(self, url):
        pg.hotkey('ctrl', 't')
        pg.typewrite(url, interval=0.05)
        pg.typewrite(['enter'])

    def browser_browse(self):
        pg.typewrite(['tab' for _ in range(5)], interval=0.05)
        pg.typewrite(['down' for _ in range(50)], interval=0.1)
