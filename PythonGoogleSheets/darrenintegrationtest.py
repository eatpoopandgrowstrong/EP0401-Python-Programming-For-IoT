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

        sheet_list[count] = client_list[count].open("IoT").worksheet('Sheet1')

    LED1state=0
    LED2state=0
    LED3state=0
    LED4state=0
    while(1):

        for count,line in enumerate(sheet_list):

            row = line.row_values(2)
            newrow =[]
            for count, line in enumerate(row):
                newrow.append(int(line))


            if(LED1state == 0 and newrow[0] == 1):
                SC.ser.write("<LED1toggle>".encode())
                LED1state=1
            elif(LED1state == 1 and newrow[0] ==0):
                SC.ser.write("<LED1toggle>".encode())
                LED1state=0
            print(row) 
            print(newrow)
            print(LED1state)  
  
   


           
            

            if(LED2state == 0 and newrow[1] == 1):
                SC.ser.write("<LED2toggle>".encode())
                LED2state=1
            elif(LED2state == 1 and newrow[1] ==0):
                SC.ser.write("<LED2toggle>".encode())
                LED2state=0
   


      

           

            if(LED3state == 0 and newrow[2] == 1):
                SC.ser.write("<LED3toggle>".encode())
                LED3state=1
            elif(LED3state == 1 and newrow[2] == 0):
                SC.ser.write("<LED3toggle>".encode())
                LED3state=0
   
    

       

            

            
            if(LED4state == 0 and newrow[3] == 1):
                SC.ser.write("<LED4toggle>".encode())
                LED4state=1
            elif(LED4state == 1 and newrow[3] == 0):
                SC.ser.write("<LED4toggle>".encode())
                LED4state=0    
        
if __name__ == "__main__":
    main()