import PyPDF2
import re
import pandas as pd

import tabula


from readers import page_finder


path = "newsite67.pdf"

pdf_obj = PyPDF2.PdfFileReader(path)
numpages = pdf_obj.getNumPages()
pages = []


pageobj = pdf_obj.getPage(1)
text = pageobj.extractText()

print(text)
