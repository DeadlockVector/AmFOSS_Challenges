
def commaCode(list1):

    #initialising string
    final_string = ''
    for i in range(len(list1)):

        #checking if we reached the end of the list
        if i == len(list1) - 1:
            final_string += ' and ' + list1[i]
        
        #second to last element
        elif i == len(list1) - 2:
            final_string += list1[i]

        else:
            final_string += list1[i] + ', '

    print(final_string)


#taking input
l1 = eval(input('Enter the list - '))
commaCode(l1)