'''
module for connection


'''

from logging import error, exception
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint


def connect_to_gsheets(sheetname):

    try:

        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.google.a"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json")

        client = gspread.authorize(creds)

        sheet = client.open(sheetname).sheet1

    except:

        raise Exception("Error connecting to sheet")


def main():

    connect_to_gsheets("IoT")


if __name__ == "__main__":

    main()