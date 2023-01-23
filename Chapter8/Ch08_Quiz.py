#import time
import time
import logging
import random

#10 questions total
correct_answers = 0
noOfQuestions = 3
for question in range(noOfQuestions):      #testing only 3 cases for now
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)


    
    chances = 3
    while chances>0:
        try:
            print('You have 8 seconds to answer - ')
            timeStart = time.time()
            answer = int(input((f'{num1}*{num2} = ')))
            endTime = time.time()
            if (endTime - timeStart) > 8:
                print('Out of time!')
                break
            
        except:
            print('Please enter an integer value')
            chances -= 1

        if answer == num1*num2:
            print('Correct!')
            correct_answers += 1
            break
        else:
            print('Incorrect!')
            chances -= 1
    else:
        print('Out of tries!')

print(f'Score - {correct_answers}/{noOfQuestions}')



