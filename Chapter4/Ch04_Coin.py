import random

numberOfStreaks = 0

for experimentNumber in range(10000):

    #creating list of tosses
    #running 100 tosses
    #adding to list
    list_tosses = []
    for tossNumber in range(100):
        toss_val = random.randint(0, 1)

        if toss_val == 0:
            toss = 'H'
        else:
            toss = 'T'

        #adding to list of tosses
        list_tosses.append(toss)

    for i in range(len(list_tosses)):

        #checking if we've reached
        #end of list
        if i == len(list_tosses) - 5:
            break

        #checks for streak
        if list_tosses[i] == 'H' and list_tosses[i+1] == 'H' and list_tosses[i+2] == 'H' and list_tosses[i+3] == 'H' and list_tosses[i+4] == 'H' and list_tosses[i+5] == 'H':
            numberOfStreaks += 1
        elif list_tosses[i] == 'T' and list_tosses[i+1] == 'T' and list_tosses[i+2] == 'T' and list_tosses[i+3] == 'T' and list_tosses[i+4] == 'T' and list_tosses[i+5] == 'T':
            numberOfStreaks += 1

#calculating percentage
#numberofstreaks/total number of tosses
#number of tosses = number of experiments * number of tosses in each experiment
print((numberOfStreaks/1000000)*100, '%')