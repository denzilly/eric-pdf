import PyPDF2
import re
import pandas as pd
import os
import tabula


from readers import page_finder

pdf_obj = PyPDF2.PdfFileReader(path)
numpages = pdf_obj.getNumPages()
pages = []


#loop through the pages and return pagenumbers that contain designated search query

if (x == 0):
    site = text[-7:]
    print(f"Site: {site}")

if (re.search(query, text) != None):
    print(f'Product list is on page {x}')
    pages.append(x)
