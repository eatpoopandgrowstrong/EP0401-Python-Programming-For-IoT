import requests



'''
Twitter API link:
    
    
Twitter API Key
LCVCMXTUR35FCJWW
'''





def main():
    
    try:
        API_Key = "LCVCMXTUR35FCJWW"
        
        for x in range(10):
            Status = f"Hello World {x}!!!!!"
        
        
            resp = requests.post(f"https://api.thingspeak.com/apps/thingtweet/1/statuses/update?api_key={API_Key}&status={Status}")
    
    except:
        raise Exception("Writing Failed")


if __name__ == "__main__":
    
    main()
    