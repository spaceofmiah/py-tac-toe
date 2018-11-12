# imports
from player import Player
from board import Board

#************************** Needed global variable ************************** #

turns = 1               # turns which denotes which player's turn it is to play
gameFlag = True         # while be used to control how game is played

pOne = pTwo = None



# ************************ Helper Method Declaration *********************** #

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



def display_top_info( ):
    '''
    displays needed information at the top of game view
    '''
    print(
    '''
    \n\n
    0000000000000000000000000000000000000000000000000000000000000
    |               * navigation around board *                 |
    0000000000000000000000000000000000000000000000000000000000000
    |                                                           |
    | `l` --- move column left        `r` --- move column right |
    | `u` --- move row up             `d` --- move row down     |
    |                                                           |
    0000000000000000000000000000000000000000000000000000000000000
    \n\n
    '''
    )




def compute_input_received( i_recieved, board_obj ):
    '''
    call appropriate method based on the input received
    '''
    if i_recieved.lower().startswith('r'):
        col_num = board_obj.move_column_to_right(i_recieved)
        row_num = board_obj.get_current_row( )
        display_top_info( )
        board_obj.set_rNc_position(col_num, row_num)

    if i_recieved.lower().startswith('l'):
        col_num = board_obj.move_column_to_left(i_recieved)
        row_num = board_obj.get_current_row( )
        display_top_info( )
        board_obj.set_rNc_position(col_num, row_num)

    if i_recieved.lower().startswith('u'):
        col_num = board_obj.get_current_column( )
        row_num = board_obj.move_row_up(i_recieved )
        display_top_info( )
        board_obj.set_rNc_position(col_num, row_num)


    if i_recieved.lower().startswith('d'):
        col_num = board_obj.get_current_column( )
        row_num = board_obj.move_row_down(i_recieved )
        display_top_info()
        board_obj.set_rNc_position(col_num, row_num)





# ********************** Implementation of game engine ******************** #


# create players ( players can only be 2 )
for i in range(1, 3, 1):
    if i == 1:
        name = input(f"{note_which_player(i)} ---- please enter your name: ")
        pOne = Player(i, name)

    if i == 2:
        name = input(f"{note_which_player(i)} ---- please enter your name: ")
        pTwo = Player(i, name)



# display top info
display_top_info( )

# draw board
board = Board( )


while( gameFlag ):
    # draw board when game starts

    # receive inputs ( compute for navigation
    # `l` --- left              `r` --- right
    # `u` --- up                `d` --- down
    recieved_input = input("\n\n>>>  ")
    compute_input_received( recieved_input, board )


    # quit from the loop
    # gameFlag = False
