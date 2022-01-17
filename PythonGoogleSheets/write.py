import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import time
import numpy as np


def main():
    
    # Setup

    # gsheet_connection_function()

    # io_connection_function()



    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.google.a"]

    creds_path = ["PythonGoogleSheets\creds\creds1.json","PythonGoogleSheets\creds\creds2.json","PythonGoogleSheets\creds\creds3.json","PythonGoogleSheets\creds\creds4.json","PythonGoogleSheets\creds\creds5.json"]

    creds1,creds2,creds3,creds4,creds5 = None, None, None, None, None
    creds_list = [creds1,creds2,creds3,creds4,creds5]

    client1, client2, client3, client4, client5 = None, None, None, None, None
    client_list = [client1, client2, client3, client4, client5]

    sheet1, sheet2, sheet3, sheet4, sheet5 = None, None, None, None, None
    sheet_list = [sheet1, sheet2, sheet3, sheet4, sheet5]

    # Setup

    for count, line in enumerate(creds_path):
        
        creds_list[count] = ServiceAccountCredentials.from_json_keyfile_name(line)
        client_list[count] = gspread.authorize(creds_list[count])

        #sheet_list[count] = client_list[count].open("IoT").sheet1
        # the .sheet1 method by default opens the first sheet, but by using .worksheet method the sheet can be specified

        sheet_list[count] = client_list[count].open("IoT").worksheet('Sheet2')

    API_DELAY = 0.01

    number = 0


    while(1):

        

        for count,line in enumerate(sheet_list):

            number += 1

            test_list = [number,number,number,number,number]

        
            #line.update('A1:B2', [[1, 2], [3, 4]])

            #line.update("A1:A2", [[1],[2]])

            #line.update("A1:E2", [["Number"], test_list])
            
            '''
            just expand as required as number of quantities increases

            idea is to just update the data row only:
            '''
            line.update("A2:E2", [test_list])
            
            print(f"Number is {number}")

        







if __name__ == "__main__":
    
    main()