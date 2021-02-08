number=int(input("input your number = "))
def Prime_number(number):
    a=number+1
    b=number -1
    '''
    if the number is greater than 4 use this math
    #6n+1=number and 6n-1=number
    #6n=number-1 and 6n=number+1
    #n=(number-1)/6 and n=(number+1)/6
    '''

    if number <4:
        #if the number is less than 4 go to this condition 
        if number==1:
            print(number,"not prime number")
        else:
            print(number,"prime number")
    elif a%6!=0 and b%6!=0:
        '''
        #if the number is greater than 4 go to this condition 
        #6n+1=number and 6n-1=number
        #6n=number-1 and 6n=number+1
        #n=(number-1)/6!=0 and n=(number+1)/6!=0
        '''
        print(number,"not prime number")
        
    else:
        print(number,"prime number")
print(Prime_number(number))