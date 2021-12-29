import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import time

def main():
    
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.google.a"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("user3\creds3.json")

    client = gspread.authorize(creds)

    sheet = client.open("IoT").sheet1

    for x in range(1000):
        data = sheet.get_all_records()

        print("3")

        pprint(data)
        time.sleep(0.9)

    









if __name__ == "__main__":
    
    main()