import matplotlib.pyplot as plt
import csv
import numpy as np

def OpenDataFile(RelativePath):
    
    with open(RelativePath, newline = "") as csvfile:
    
        Reader = csv.reader(csvfile, delimiter = ',')
        Seconds, Temperature, Humidity = [], [], []
        
        #print(Reader.info)
        for row in Reader:
            
            print(type(row[0]))
            Seconds.append(int(row[0]))
            Temperature.append(int(row[1]))
            Humidity.append(int(row[2]))
        
    #print(Seconds)
    
    return Seconds,Temperature,Humidity


def main():
    
    RelativePath = "sensordata.txt"
    SecondsList, TemperatureList, HumidityList = OpenDataFile(RelativePath)
    
    #fig = plt.figure()
    
    
    
    '''
    plt.subplot(111)
    
    ax1 = plt.subplot(111)
    
    #plt.yticks([y for y in range(100)])
    
   
    ax1.plot(SecondsList, TemperatureList, HumidityList)
    #ax1.set_ylabel([x for x in range(1,100)])
    #ax1.plot(SecondsList, )
    #ax1.set_ylim(0,100)
    #print(TemperatureList)
    '''
    fig, ax = plt.subplots()
    
    ax.plot(SecondsList, TemperatureList, color = 'green', label = 'Line 1')
    ax.plot(SecondsList, HumidityList, color = 'red', label = 'Line 2')
    print(HumidityList)
    #print(HumidityList.size())
    ax.legend(loc = 'upper left')

    
    plt.legend()
    
    plt.show()

    #print(SecondsList, TemperatureList, HumidityList)

    # Plotting
    



if __name__ == "__main__":
    
    main()