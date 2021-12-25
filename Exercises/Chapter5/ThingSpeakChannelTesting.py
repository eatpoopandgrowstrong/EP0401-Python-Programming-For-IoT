import requests


def main():
    
    Write_API_Key = "CN2YHCUSME1URZK5"
    Read_API_Key = ""
    Placeholder1 = [x for x in range(1,11)]
    Placeholder2 = [x for x in range(10,21)]
    ChannelID = 1570748
    # Private Writing
    
    try:
        
        resp = requests.get(f"https://api.thingspeak.com/update?api_key={Write_API_Key}&field1={Placeholder1}&field2={Placeholder2}" )

    except:
        
        raise Exception("Error writing to Fields 1 and 2")
      
        
    # Private Reading
    '''
    try:
        
        resp = requests.delete (f"")
        
    except:
        
        raise Exception("Error Reading from Channels")
    '''
    
    # Deleting Channel Data
    
    '''
    try:
        
        resp = requests.delete(f"https://api.thingspeak.com/channels/{ChannelID}/feeds.json?api_key=JLSJ8EXZBXGR95WI")
        
    except:
        
        raise Exception("Error Deleting Data from channel")
    '''
if __name__ == "__main__":
    
    main()
