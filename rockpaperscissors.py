import random

playing  = True
while playing:
    playerchoice = input('Choose Rock, Paper, or Scissors: ')
    compchoice = random.choice(['Rock', 'Paper', 'Scissors'])
    playerchoice=playerchoice.title()
    if compchoice == playerchoice:
        print('I chose', compchoice, 'too. Tie')
    elif compchoice == 'Paper' and playerchoice == 'Scissors':
        print('I chose', compchoice, 'You win!')
        break
    elif compchoice == 'Scissors' and playerchoice == 'Rock':
        print('I chose', compchoice, 'You win!')
        break
    elif compchoice == 'Rock' and playerchoice == 'Paper':
        print('I chose', compchoice, 'You win')
        break
    else:
        print('I chose', compchoice, 'You lose')