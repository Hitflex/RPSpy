import random, sys
print('Rock, Paper, Scissors')
wins = 0
losses = 0
ties = 0
while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        computerInput = random.randint(1, 3)
        if computerInput == 1:
            computerInput = 'r'
            computerDisplay = 'ROCK'
        elif computerInput == 2:
            computerInput = 'p'
            computerDisplay = 'PAPER'
        elif computerInput == 3:
            computerInput = 's'
            computerDisplay = 'SCISSORS'
        print('Enter your move: [r]ock, [p]aper, [s]cissors and [q]uit')
        playerInput = input()
        if playerInput == 'q':
            sys.exit()
        elif playerInput == 'r' or playerInput == 'p' or playerInput == 's':
            if playerInput == 'r':
                playerDisplay = 'ROCK'
            if playerInput == 'p':
                playerDisplay = 'PAPER'
            if playerInput == 's':
                playerDisplay = 'SCISSORS'
            break
    print('You choose '+playerDisplay+' Computer choose '+computerDisplay)
    if playerInput == computerInput:
        print('it\'s a tie')
        ties = ties + 1
    elif playerInput == 'r' and computerInput == 's':
        print('You win!')
        wins = wins + 1
    elif playerInput == 's' and computerInput == 'p':
        print('You win!')
        wins = wins + 1
    elif playerInput == 'p' and computerInput == 'r':
        print('You win!')
        wins = wins + 1
    elif playerInput == 'r' and computerInput == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerInput == 'p' and computerInput == 's':
        print('You lose!')
        losses = losses + 1
    elif playerInput == 's' and computerInput == 'r':
        print('You lose!')
        losses = losses + 1
