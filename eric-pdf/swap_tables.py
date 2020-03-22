
import re
import pandas as pd
import os
import tabula
import pdfplumber



path = os.getcwd() + "\\data\\swaps\\s4.pdf"


#### FIND THE NUMBER OF EXPANSION AND WAREHOUSE TABLES


def WhEx_countfinder(path, pages):




    def count_under(text_list):
        count = 0
        for x in text_list:
            if len(x) < 22:
                count += 1

        return count




    pdf = pdfplumber.open(path)
    page = pdf.pages[3]
    text = page.extract_text().splitlines()
    lent = []

    #FIND LOCATION OF WH and EXPANSION headers, to determine how many tables to extract
    expIN = False
    whIN = False


    for x in text:
        lent.append(len(x))

        if "FOR EXPANSION" in x:
            indexEX = text.index(x)
            expIN = True
            print(len(x))
            print(f"found ex{indexEX}")


        if "TO WH" in x:
            indexWH = text.index(x)
            whIN = True
            print(f"found wh{indexWH}")

    try:
        if whIN == True:
            EX_tablecount = count_under(text[indexEX+1:indexWH])
        else:
            EX_tablecount = count_under(text[indexEX+1:])

    except NameError:
        print("No EX Tables")
        EX_tablecount = 0


    try:
        WH_tablecount = count_under(text[indexWH+1:])

    except NameError:
        print("No WH Tables")
        WH_tablecount = 0



    return EX_tablecount, WH_tablecount
