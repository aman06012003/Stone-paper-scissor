
import random
def plays():
    user = input("What's your choice ? ('r' for rock,'s' for scissors, 'p' for paper)  ")
    computer = random.choice(['r','s','p'])

    if user == computer:
        print('Its a tie....')

    # r>s, s>p, p>r
    if is_win(computer, user):
        return 'Congrats you won!!'

    return 'Sorry you lost'

def is_win(opponent, player):
    # return true if oppennent wins
    if (opponent == 'r' and player == 's') or (opponent == 's' and player == 'p') or (opponent == 'p' and player == 'r'):
        return True



print(plays())
