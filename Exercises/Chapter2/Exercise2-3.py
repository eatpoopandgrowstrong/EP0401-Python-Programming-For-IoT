# Exercise 2.3 - Will I be rich?

'''
Just bruteforce this?

Start working at 25
3000 initial salary
3 month bonus in addition to regular salary
Save 30% and invest it for a 10% return?

Pay increases by 10% each year as well

'''

def main():
    
    Age = 25
    Salary = 3000
    AmountAfterInvestment = 0
    while(1000000 > AmountAfterInvestment):
        
    
        AnnualSalary = Salary * (12 + 3)
        AnnualSaving = (AnnualSalary * 0.3)
        
        AmountBeforeInvestment =  AnnualSaving + AmountAfterInvestment
        AmountAfterInvestment = AmountBeforeInvestment * 1.1
    
        Age +=1
        
        Salary *= 1.1
        
        '''
        This is hot garbage
        Use some other form of iteration instead?
        '''

    print("Insert guy here will be " + str (Age) + " when he has >1mil dollars")
    
    
    
    
#def main():
    
    


if __name__ == "__main__":
    
    main()