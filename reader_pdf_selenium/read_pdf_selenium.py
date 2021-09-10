from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from pywinauto import application, keyboard
from selenium.webdriver.common.keys import Keys
import sys
import win32clipboard
import traceback
from time import sleep

class PDFReader:
    def __init__(self):
        self.ie_app = None
        self.hwnd = None
        return

    def get_clipboard_data(self):

        action_delay = 0.01
        win32clipboard.OpenClipboard()
        sleep(action_delay)
        data = win32clipboard.GetClipboardData()
        win32clipboard.EmptyClipboard()
        win32clipboard.CloseClipboard()
        return data

    def open_chrome(self, filepath):

        content = ''

        try:
            driver = webdriver.Chrome(ChromeDriverManager(chrome_type = ChromeType.CHROMIUM).install())
            sleep(1)
            driver.get(filepath)
            sleep(1)

            select_all = "^a"
            copy_keys = "^c"
            driver.maximize_window()
            driver.implicitly_wait(2)

            keyboard.send_keys(select_all)
            sleep(1)
            keyboard.send_keys(copy_keys)

        except Exception as exc:
            print(traceback.format_exc(), file=sys.stderr)
            print(exc, file=sys.stderr)

        finally:
            # content = self.get_clipboard_data()
            print('finalizou')

        return content