# imports
from player import Player


gameFlag = True         # while be used to control how game is played
turns = 1               # turns which denotes which player's turn it is to play



def note_which_player( turns ):
    '''
    helps to tell which players turn it is
    '''
    if turns == 1:
        return "playerOne"
    if turns == 2:
        return "playerTwo"



def swap_player_turn( ):
    '''
    changes turns of players to play
    '''
    # use the global turns variable
    global turns

    if turns == 1:
        turns += 1

    elif turns == 2:
        turns -= 1



# create players ( players can only be 2 )
for i in range(1, 3, 1):
    if i == 1:
        name = input(f"{note_which_player(i)} ---- please enter your name: ")
        pOne = Player(i, name)

    if i == 2:
        name = input(f"{note_which_player(i)} ---- please enter your name: ")
        pTwo = Player(i, name)



swap_player_turn()
print(note_which_player(turns))
swap_player_turn()
print(note_which_player(turns))

# while( gameFlag ){
#
#
# }
