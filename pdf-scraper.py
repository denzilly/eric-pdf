import tabula

import xlsxwriter
import PyPDF2
import re
import pandas as pd


import os
import fnmatch

from readers import read_page_new




def gen_file_list(query):

    filename_list = []

    for file in os.listdir(os.getcwd() + "\\data\\"):
        if fnmatch.fnmatchcase(file, f"*{query}*"):
            filename_list.append(file)

    return(filename_list)







def write_to_excel(RBS_list):


    headers = ["siteID", "Date"]
    row_list = [headers]
    for x in range(35):
        headers.extend([f"Unit Code {str(x)}", f"Product Code {str(x)}", f"Serial Number Code {str(x)}", ])


################## NEW #############################
    for x in RBS_list:
        row_list.append(read_page_new("eric-pdf\\data\\" + x))

    with xlsxwriter.Workbook('output\\NEW.xlsx') as workbook:
        new_sites = workbook.add_worksheet()

        for row_num, data in enumerate(row_list):
            new_sites.write_row(row_num, 0, data)









if __name__ == '__main__':

    RBS_list = gen_file_list("RBS")
    #SWAP_list = gen_file_list("Swap")
    #EXP_list = gen_file_list("Exp")

    write_to_excel(RBS_list)
