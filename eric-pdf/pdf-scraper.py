import tabula

import xlsxwriter
import PyPDF2
import re
import pandas as pd


import os
import fnmatch

from readers import read_page_new, read_page_swap






def gen_file_list(query):

    filename_list = []
    print(os.getcwd())
    for file in os.listdir(os.getcwd() + "\\data\\"):
        if fnmatch.fnmatchcase(file, f"*{query}*"):
            filename_list.append(file)

    return(filename_list)


#Option 1 = RBS, Option 2 = SWAP, Option 3 = EXP
def write_to_excel(RBS_list, option):


    headers = ["siteID", "Date"]

    for x in range(35):
        headers.extend([f"Unit Code {str(x)}", f"Product Code {str(x)}", f"Serial Number Code {str(x)}", ])




################## NEW #############################
    #new
    if (option == 1):

        row_list = [headers]

        for x in RBS_list:
            row_list.append(read_page_new(os.getcwd() + "\\data\\" + x))

        with xlsxwriter.Workbook(os.getcwd() + '\\output\\NEW.xlsx', {'nan_inf_to_errors': True}) as workbook:
            new_sites = workbook.add_worksheet()

            for row_num, data in enumerate(row_list):
                new_sites.write_row(row_num, 0, data)

    #swap
    if (option == 2):

        ex_row_list = [headers]
        wh_row_list = [headers]

        for x in SWAP_list:
            ex_serials_list, wh_serials_list = read_page_swap(os.getcwd() + "\\data\\" + x)


            ex_row_list.append(ex_serials_list)
            wh_row_list.append(wh_serials_list)

        with xlsxwriter.Workbook(os.getcwd() + '\\output\\SWAPS.xlsx', {'nan_inf_to_errors': True}) as workbook:
            Expansion = workbook.add_worksheet('Expansion')
            TO_WH = workbook.add_worksheet('To WH')

            for row_num, data in enumerate(ex_row_list):
                Expansion.write_row(row_num, 0, data)

            for row_num, data in enumerate(wh_row_list):
                TO_WH.write_row(row_num, 0, data)


        #print("not yet implemented")




    #Ex
    if (option == 3):
        print("not yet implemented")









if __name__ == '__main__':

    RBS_list = gen_file_list("RBS")
    SWAP_list = gen_file_list("Swap")
    #EXP_list = gen_file_list("Exp")

    print("Which option?")
    option = 2

    #write_to_excel(RBS_list, 1)
    write_to_excel(SWAP_list, 2)
