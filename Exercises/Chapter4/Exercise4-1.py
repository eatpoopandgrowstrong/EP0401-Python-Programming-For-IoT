import matplotlib.pyplot as plt



def main():
    
    Items = ["Food", "Clothing", "Transport", "Rent", "Entertainment"]
    Amounts = [35, 20, 21, 100, 50]
    XList = [x for x in range(1,5+1)]
    
    print(XList)
    
    plt.bar(Items, Amounts)
    #plt.xticks([x for x in range (1,5+1)])
    plt.show()
        
    

if __name__ == "__main__":
    
    main()
    