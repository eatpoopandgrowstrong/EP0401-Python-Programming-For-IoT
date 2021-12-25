import time 
import requests
import json

'''
https://thingspeak.com/channels/1569101/

H5HK0AU3GWKLSX7L

BKY0NBPBPIFMZ7QF
'''

def main():
        
    try:
        resp = requests.get("https://api.thingspeak.com/channels/1569101/feeds.json?results=10" )
        #print(type(resp))
        print(resp.text)
        print(type(resp.text))
    
        results = json.loads(resp.text)
        #print(results)
        
        print(type(results))
        print(results)
        print(results.keys())
        
        for x in range(10):
            print(f"Field 1 is: {results['feeds'][x]['field2']} , Field 2 is: {results['feeds'][x]['field2']}")
        
        '''
        print(results['feeds'][0]['field1'])
        print(results['feeds'][1]['field2'])
        '''
        
        '''
        Need to figure out how the dictionary looks like, why are there multiple keys here
        Its a nested dictionary?
        '''
        
    except:    
        print("Receiving Failed")
    

if __name__ == "__main__":
    
    main()
    
    
    
    
    