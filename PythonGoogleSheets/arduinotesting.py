import SerialComm as SC
import importlib
import time

importlib.reload(SC)
'''
SerialComm module is a bit dated, uses camel case
Needs some rewriting to just connect everything atuomatically, shouldn't need to have write another function in main

'''



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

    # Setup
    arduino_connection()

    '''
    Just need to port/merge this into the main script

    Guide to using SC.ser.write()
    Since we are using start and endmarkers,  we will need to include them with the string that we use

    An example:
    <LEDON>
    So the Arduino will recognise and read it as:
    LEDON

    Something to note is that messages sent without the start and endmarker will result in the message not
    being recognised
    '''
    
    SC.ser.write("<Testing>".encode())
    SC.ser.write("<LED1toggle>".encode())
    SC.ser.write("<LED2toggle>".encode())
    SC.ser.write("<LED3toggle>".encode())
    SC.ser.write("<LED4toggle>".encode())
    time.sleep(1)
    SC.ser.write("<LED1toggle>".encode())
    SC.ser.write("<LED2toggle>".encode())
    SC.ser.write("<LED3toggle>".encode())
    SC.ser.write("<LED4toggle>".encode())
    # Code to disconnect from Arduino if script stops
    # Have to physically unplug and re-plug if Arduino isn't disconnected
    try:
        SC.DisconnectFromArduino()
    except:
        pass

if __name__ == "__main__":

    main()