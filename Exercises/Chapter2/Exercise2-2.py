# Exercise 2.2 - Multiplication Table

def main():

    print("Enter an integer")
    
    Iterations = 15                                                             # Not sure how many iterations the user exercise wants, create some placeholder value to be edited
    
    UserInputString = input()                                                   # The Input() method returns a string
    
    UserInputInteger = int (UserInputString)                                    # Convert the string to an integer for computation
                  
    # print("The User Input Number is " + str (UserInputInteger))
    
    # Something to note here is that range() indexing starts from 0 by default, use the range(start,end)
    
    for x in range(1,Iterations + 1):                                           # Add 1 for the end since it'll stop 1 short since index from 0
        
        #if x == UserInputInteger: break
    
        OutputString = str (x * UserInputInteger)
        
        print(UserInputString + " x " + str(x) + " = " + OutputString)


if __name__ == "__main__":
    
    main()