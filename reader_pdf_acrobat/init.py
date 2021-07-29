import os
import base64

# from teste import PDFReader
from read_pdf import PDFReader

file_parser = PDFReader()

content = file_parser.parse_acrobat(os.path.abspath(os.getcwd())+'\\test_pdf.pdf')

# print(content)
print(content.encode("utf-8"))