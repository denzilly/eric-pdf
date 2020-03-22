import PyPDF2
import re
import pandas as pd

import tabula

from swap_tables import WhEx_countfinder




## Find on which page your designated query lives
def page_finder(path, query):


    #import pdf object, get number of pages
    pdf_obj = PyPDF2.PdfFileReader(path)
    numpages = pdf_obj.getNumPages()
    pages = []


    #loop through the pages and return pagenumbers that contain designated search query
    for x in range(0, numpages):
        pageobj = pdf_obj.getPage(x)
        text = pageobj.extractText()
        #print(text)
        #search = re.search(query, text)

        if (x == 0):
            site = text[-7:]
            print(f"Site: {site}")

        if (re.search(query, text) != None):
            print(f'Product list is on page {x}')
            pages.append(x)




    return(pages,site)






def read_page_new(path):

    pages, site = page_finder(path, "PRODUCT LIST")
    df = tabula.read_pdf(path, pages=pages[0]+1)
    date = "unknown"

    #if (df[0].iloc[1,1] =
    try:

        if(str(df[0].iloc[2,2][0]) == "2"):
            date = df[0].iloc[2,2]

    except:
        print("date search error")


    serials_list = [site, date]

    for x in df[1:]:
        try:
            if pd.notna(x.iloc[0,0]):

                print(x.shape)

                #Iterate over the rows of each dataframe, and add values to a list in order, but only if unit ID is nonblank
                #If no serial number, or no third column exists, adds "no serial number" for SN

                try:
                    for index, row in x.iterrows():


                        if pd.notna(row[1]):

                            if pd.notna(row[2]):

                                serials_list.extend([row[0],row[1],row[2]])

                            else:
                                try:
                                    serials_list.extend([row[0],row[1],row[3]])
                                except IndexError:
                                    #print("out of bounds")
                                    serials_list.extend([row[0],row[1],'No serial number'])

                        #print(dict)
                except IndexError as e:
                    print(f"internal indexerror: {e}")
                    continue
            else:
                #print("wrong table")
                continue
        except IndexError:
                print("external indexerror")
                continue
    return(serials_list)


def read_page_swap(path):
    print(path)


    pages, site = page_finder(path, "PRODUCT LIST")
    print(pages)
    try:
        df = tabula.read_pdf(path, pages=pages[0]+1)
    except IndexError as e:
        print(f"Index error, probably weird table format: {e}")
        df = pd.DataFrame()
    date = "unknown"

#DATE SECTION
    try:

        if(str(df[0].iloc[2,2][0]) == "2"):
            date = df[0].iloc[2,2]

    except:
        print("date search error")





    ex_tcount, wh_tcount = WhEx_countfinder(path,pages[0]+1)
    print(ex_tcount,wh_tcount)



    def gen_serial_list(df, range_lower, range_upper):

        serials_list = [site, date]

        for x in df[range_lower : range_upper]:
            print(df)
            try:
                if pd.notna(x.iloc[0,0]):



                    #Iterate over the rows of each dataframe, and add values to a list in order, but only if unit ID is nonblank
                    #If no serial number, or no third column exists, adds "no serial number" for SN

                    try:
                        for index, row in x.iterrows():


                            if pd.notna(row[1]):

                                if pd.notna(row[2]):

                                    serials_list.extend([row[0],row[1],row[2]])

                                else:
                                    try:
                                        serials_list.extend([row[0],row[1],row[3]])
                                    except IndexError:
                                        #print("out of bounds")
                                        serials_list.extend([row[0],row[1],'No serial number'])

                            #print(dict)
                    except IndexError as e:
                        print(f"internal indexerror: {e}")
                        continue
                else:
                    #print("wrong table")
                    continue
            except IndexError as e:
                    print(f"external indexerror: {e}")
                    continue
        return(serials_list)


    #BOTH EX AND WH EXIST
    if (ex_tcount > 0 and wh_tcount > 0):
        ex_serials_list = gen_serial_list(df, 1, 1 + ex_tcount)
        wh_serials_list = gen_serial_list(df, 1 + ex_tcount, 1 + ex_tcount + wh_tcount)

    # ONLY EX TABLE
    if (ex_tcount > 0 and wh_tcount == 0):
        ex_serials_list = gen_serial_list(df, 1, 1 + ex_tcount)
        wh_serials_list = []

    # ONLY WH TABLE
    if (ex_tcount == 0 and wh_tcount > 0):
        ex_serials_list = []
        wh_serials_list = gen_serial_list(df, 1, 1 + wh_tcount)

    if (ex_tcount == 0 and wh_tcount == 0):
        ex_serials_list = []
        wh_serials_list = []
        print("not a swap file")

    return(ex_serials_list, wh_serials_list)





def read_page_exp(path):
    print("done")
