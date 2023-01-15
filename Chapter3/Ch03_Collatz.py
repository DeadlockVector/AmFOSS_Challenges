
#defining collatz
def collatz(number):
    if (number%2 == 0):
        val = number//2
    else:
        val = 3*number + 1
    
    print(val)
    return val

#checking if int entered
try:
    n = int(input('Enter an integer - '))

    while True:

        #calling collatz
        #reassigning returned value back to parameter
        n = collatz(n)

        if n == 1:
            break

except:
    print('Please run the program and enter a god awful integer this time')




