import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import time

def main():
    
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

        sheet_list[count] = client_list[count].open("IoT").sheet1

    API_DELAY = 0.01

    while(1):

        for count,line in enumerate(sheet_list):

            data = line.get_all_records()

            pprint(data)
            #time.sleep(API_DELAY)

    '''
    Idea is just to read the entire sheet at once, uses 1 API call instead of multiple individual calls
    Just have to do some manipulation/planning for the formatting
    
    Have this chucked on raspberry pi, raise a flag if anything changes, do some if else or switch statements

    Workflow -> Code on PC, run testing on raspberry pi -> Merge to main

    


    '''






if __name__ == "__main__":
    
    main()