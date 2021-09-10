import os

from read_pdf_selenium import PDFReader

file_parser = PDFReader()

content = file_parser.open_chrome(os.path.abspath(os.getcwd())+'\\test_pdf.pdf')

print(content.encode("utf-8"))