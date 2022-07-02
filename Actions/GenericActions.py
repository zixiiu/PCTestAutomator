from abc import abstractmethod
import pyautogui


class GenericActions():

    def __init__(self):
        pyautogui.PAUSE = 1
        pyautogui.FAILSAFE = True

    @abstractmethod
    def launch_app_with_search(self, kw):
        pass

    @abstractmethod
    def launch_ms_word(self):
        pass

    @abstractmethod
    def launch_ms_ppt(self):
        pass

    @abstractmethod
    def ms_ppt_actions(self):
        pass

    @abstractmethod
    def type_and_remove(self):
        pass

    @abstractmethod
    def launch_ms_excel(self):
        pass

    @abstractmethod
    def ms_excel_cal(self):
        pass

    @abstractmethod
    def launch_browser(self):
        pass

    @abstractmethod
    def browser_new_tab(self, url):
        pass

    @abstractmethod
    def browser_browse(self):
        pass

    @abstractmethod
    def browser_search(self, kw):
        pass

    @abstractmethod
    def launch_qq(self):
        pass

    @abstractmethod
    def launch_netease_music(self):
        pass

