import time 
import requests
import random

'''
https://thingspeak.com/channels/1569101/

H5HK0AU3GWKLSX7L

BKY0NBPBPIFMZ7QF
'''

def main():
    
    #random.seed(1)
    #print(random.randrange(1,5,1))
    API_Key = "H5HK0AU3GWKLSX7L"
    Placeholder1 = [x for x in range(1,11,1)]
    Placeholder2 = [x for x in range(1,11,1)]
    print(Placeholder1)
    
    for x in range(10):
        print("Sending to ThingSpeak:")
        print(f"Placeholder1 = {Placeholder1[x]}, Placeholder2 = {Placeholder2[x]}")
        
        resp = requests.get(f"https://api.thingspeak.com/update?api_key={API_Key}&field1={Placeholder1[x]}&field2={Placeholder2[x]}" )
    
        time.sleep(16)
    
    print("Data Output Completed")
    #resp = requests.get(f"https://api.thingspeak.com/update?api_key=H5HK0AU3GWKLSX7L&field1={Placeholder1}&field2={Placeholder2}" )
    # For free thingspeak, channels are limited to 15s, just use 16 to be safe
    
if __name__ == "__main__":
    
    main()
    