import numpy as np

def main():

    print("Enter an integer")
    
    UserInputString = input()                                                   # The Input() method returns a string
    
    UserInputInteger = int (UserInputString)                                     # Convert the string to an integer for computation
                  
    # print("The User Input Number is " + str (UserInputInteger))
    
    # Something to note here is that range() indexing starts from 0
    
    for x in range(UserInputInteger):
        
        if x == UserInputInteger: break
        
        print(UserInputString + " x " + x )
    
    
    


if __name__ == "__main__":
    
    main()