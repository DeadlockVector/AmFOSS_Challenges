import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    toss = random.randint(0, 1)     # 0 is tails, 1 is heads
    toss_dict = {0:"heads", 1:"tails"}

if toss_dict[toss].lower() == guess:
    print('You got it!')

else:
    print('Nope! Guess again!')
    guesss = input()
    if toss_dict[toss].lower() == guesss:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')