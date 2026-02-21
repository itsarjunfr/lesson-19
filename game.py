import random
x = random. randint(1,11)
playing = True
while playing: 
    y = int(input('Pick a random number from 1 to 10: '))
    if y==x:
        print('Congrats!', x, 'was the number!')
        break
    else:
        print('Try again.')
    