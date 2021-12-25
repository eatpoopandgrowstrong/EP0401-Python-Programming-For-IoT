import matplotlib.pyplot as plt
import pandas as pd


def OpenDataFile(RelativePath):
    
    df = pd.read_csv(RelativePath, header = None)
    df.columns = ["Seconds", "Temperature", "Humidity"]

    return df


def main():
    
    RelativePath = "sensordata.txt"
    Data = OpenDataFile(RelativePath)
    
    print(Data)
    print(Data["Temperature"].mean())

    print(Data["Temperature"])
    
    '''
    plt.show()

    '''

if __name__ == "__main__":
    
    main()
    