import logging
import sys, winerror, os
import pythoncom
import win32com.client as win32client
import win32com.client.makepy as win32ClientMake
from win32com.client.dynamic import ERRORS_BAD_CONTEXT
import traceback
from time import sleep

ERRORS_BAD_CONTEXT.append(winerror.E_NOTIMPL)

class PDFReader:
    def __init__(self):
        self.reqs_path = "log/PDF.log"
        return

    def parse_acrobat(self, filepath):

        content = None

        try:
            logging.basicConfig(filename=self.reqs_path, encoding='utf-8', level=logging.DEBUG)
            win32ClientMake.GenerateFromTypeLibSpec('AcroPDF.PDF')
            avDoc = win32client.DispatchEx('AcroExch.AVDoc')
            logging.debug('======================================')
            logging.debug(filepath)

            avDoc.Open(filepath, "")
            pdDoc = avDoc.GetPDDoc()
            numPage = pdDoc.GetNumPages()
            jObject = pdDoc.GetJSObject()

            word_file = filepath.replace('.pdf','.docx')
            jObject.SaveAs(word_file, "com.adobe.acrobat.docx")

            pythoncom.CoInitialize()
            word = win32client.gencache.EnsureDispatch(
                        "Word.Application")

            word.Visible = False
            sleep(1)
            doc = word.Documents.Open(r'"%s"' % (word_file))
            content = doc.Content.Text

            logging.debug(content)
            logging.debug(numPage)

        except Exception as exc:
            print(traceback.format_exc(), file=sys.stderr)
            print(exc, file=sys.stderr)

        finally:
            jObject = None
            pdDoc = None
            avDoc = None
            doc.Close(-1)
            word.Quit()
            del word
            os.remove(word_file)
            pythoncom.CoUninitialize()

        return content