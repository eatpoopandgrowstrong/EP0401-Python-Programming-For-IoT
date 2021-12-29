import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import time

def main():
    
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.google.a"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json")

    client = gspread.authorize(creds)

    sheet = client.open("tutorial").sheet1

    for x in range(1000):
        data = sheet.get_all_records()

        print(data)

        pprint(data)
        time.sleep(1.5)

    '''
    
    row = sheet.row_values(3)

    print(row)

    pprint(row)
    '''
    

    '''
    How to write data:


    How to read data:


    
    
    
    '''
    









if __name__ == "__main__":
    
    main()