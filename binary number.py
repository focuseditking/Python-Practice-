'''This portion of the code is used to accept a value for the user and validate
if it is an actual number and whether or not the entered value is within the
acceptable range
'''
enum = ''
while True:
    enum = (input ("Enter an number between 0 - 255 and I'll convert it to a binary number: "))
    if enum.isdigit():
        if 0 <= int(enum) <=255:
            break
    
    print('Invalid Input, Try again:')
    


'''Now we need to take the interger and convert it to its binary form and print it without the "ob"
that preceed it. 
'''
def dec_to_bin(num='0'):
    num = int(num)
    num = bin(num)
    num = num[2:]
    numLen = len(num)

    #print (numLen)
    #print (num)

    zeros = 8 - numLen
    while zeros > 0:
        num = '0' + num
        zeros -= 1
    return num

#print(num)

print(dec_to_bin(enum))

'''
num = (input ("Enter an number and I'll convert it to a binary number: "))
x = num.isdigit()
while x == False:
    numx = input("Invalid Entry... Try again : ")
    if numx.isdigit == True:
        num = int(num)
        low = 0
        high = 256
        num = bin(num)
        num = num[2:]
        numLen = len(num)


        if low<= num <= high:
            print (numLen)
            print (num)
    else:
        num = False
    #if x!= True:
        #num = (input ("That is not a vaild entry: \nEnter an number and I'll convert it to a binary number: "))

        
        #print ("Nope")
        #break
    
  #  else:
    num = int(num)
    low = 0
    high = 256
    num = bin(num)
    num = num[2:]
    numLen = len(num)


    if low<= num <= high:
        print (numLen)
        print (num)

''' '''zeros = 8 - numLen
        while zeros > 0:
            num = '0' + num
            zeros -= 1

        print (num)
    else: ("Chose a number between 1 and 256")
print ("I said enter a number")
while numLen > 0:
    if numLen < 8:
    print( [0,numLen,0])
print (num)
'''

''' Ask the user for and IP address
and convert it to binary'''
