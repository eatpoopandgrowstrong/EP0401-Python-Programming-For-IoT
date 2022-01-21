import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import time
import SerialComm as SC
import importlib
importlib.reload(SC)

def arduino_connection():

    try:

        ArduinoPortsList = SC.ListArduinoConnectedPorts()
        SC.ConnectToArduino(ArduinoPortsList, 115200, 0.01)
        
    except:

        raise Exception("Error Connecting to Arduino")
    
    Data = SC.ReceiveStringWithStartAndEndMarkers()
    print(Data)

    SC.CommCheck()

def main():

    arduino_connection()
    
    # TODO: Move all the gsheet connection stuff to its own function

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

        sheet_list[count] = client_list[count].open("IoT").worksheet('Sheet1') # Specifically open "Sheet1" on the google sheets

   
    LEDstate_list = [0, 0, 0, 0] # There are 4 LEDs, list of the 4 LED states
    while(1):

        for count,line in enumerate(sheet_list):

            string_row = line.row_values(2) # row_values returns a list of strings
            
            int_list = [int(x) for x in string_row] #convert the string elements to int

            for count,line in enumerate(int_list): # iterate through the list

                if(line != LEDstate_list[count]):
                    
                    SC.ser.write(("<LED" + str(count+1) + "toggle>").encode())
                    LEDstate_list[count] = line

        
if __name__ == "__main__":
    main()