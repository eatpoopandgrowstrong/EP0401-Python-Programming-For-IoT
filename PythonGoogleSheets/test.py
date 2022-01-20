'''
Test = ['2','2']
newtest = []
for count,line in enumerate(Test):

    newtest.append(int(line))

print(newtest)
'''
iterablelist = [0,1,2,3]
stringlist = []

DemoList = [1,1,0,0] # FIrst 2 off Last 2 On

'''
for x in range(len(iterablelist)):
    stringlist.append(str(iterablelist[x]))
'''

for count,line in enumerate(iterablelist):
    stringlist.append(str(line+1))

    #print(stringlist[count])
    
    #SC.ser.write(("LED" + stringlist[count] + "toggle").encode())
    #print(("LED" + stringlist[count] + "toggle"))

#ListComprehension = [x+1 for x in range(4)]

Potato = [x == 1 for x in DemoList]
for count,line in enumerate(Potato):
    if(line == False):
        print(("LED" + str(count+1) + "toggle"))

#print(ListComprehension)
#print(Potato)
#TODO modify to use list comprehension




# Desired output
#SC.ser.write("LED1toggle".encode())
#SC.ser.write("LED2toggle".encode())
#SC.ser.write("LED3toggle".encode())
#SC.ser.write("LED4toggle".encode())











#print(stringlist)
#print(type(stringlist))