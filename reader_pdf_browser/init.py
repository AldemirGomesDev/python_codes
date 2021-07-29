import os

from test import PDFReader

file_parser = PDFReader()

content = file_parser.open_ie(os.path.abspath(os.getcwd())+'\\test_pdf.pdf')

print(content.encode("utf-8"))