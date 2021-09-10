from pywinauto import application, keyboard
import sys
import win32clipboard
import win32com.client as win32client
import win32gui
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

        self.hwnd = win32gui.GetForegroundWindow()
        self.ie_app = win32client.Dispatch("WScript.Shell")

        content = ''

        try:
            self.ie_app.Run('chrome')

            sleep(0.1)
            self.ie_app.AppActivate('chrome')
            self.ie_app.SendKeys(filepath, 0)
            self.ie_app.SendKeys("{Enter}", 0)

            select_all = "^a"
            copy_keys = "^c"

            sleep(1)
            keyboard.send_keys(select_all)
            sleep(1)
            keyboard.send_keys(copy_keys)



            sleep(1)
            #self.ie_app.SendKeys("^{F4}", 0)
            win32gui.SetForegroundWindow(self.hwnd)

            self.ie_app.AppActivate(str(self.hwnd))

        except Exception as exc:
            print(traceback.format_exc(), file=sys.stderr)
            print(exc, file=sys.stderr)

        finally:
            content = self.get_clipboard_data()

        return content

    def open_ie(self, filepath):

        self.ie_app = win32client.Dispatch('InternetExplorer.Application')

        content = ''

        try:
            self.ie_app.Visible = 1
            self.ie_app.navigate(filepath)

            pdfViewer = self.ie_app.Document.embeds[0]
            content = pdfViewer.Print()

        except Exception as exc:
            content =  exc
            print(traceback.format_exc(), file=sys.stderr)
            print(exc, file=sys.stderr)

        finally:
            self.ie_app.Quit()

        return content