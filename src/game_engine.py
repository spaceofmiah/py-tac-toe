# imports
import sys
from player import Player
from board import Board

#************************** Needed global variable ************************** #

turns = 1               # turns which denotes which player's turn it is to play
gameFlag = True         # while be used to control how game is played


pOne = pTwo = playingPlayer = None



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
    its_player_turn = get_playing_player().playerName

    print(
    f'''
    \n\n
    00000000000000000000000000000000000000000000000000000000000000000000000
    |                        * Game Action Keys*                          |
    00000000000000000000000000000000000000000000000000000000000000000000000
    |                                                                     |
    | (** navigate board **)                                              |
    |                                                                     |
    | `l` --- move column left        `r` --- move column right           |
    | `u` --- move row up             `d` --- move row down               |
    |                                                                     |
    | (** Play and Unplay **)                                             |
    |                                                                     |
    | `m` --- mark current row and column position on board as played     |
    |                                                                     |
    00000000000000000000000000000000000000000000000000000000000000000000000

                             ** { its_player_turn }'s turn **
    \n\n
    '''
    )



def get_playing_player( ):
    '''
    returns the player who's currently playing
    '''
    if turns == 1:
        return pOne
    return pTwo




def check_win( board, player_obj ):
    '''
    check if there is a win. A win can occur Horizontally, Vertically, &
    Diagonally. if there is a win it returns True and the pattern in which
    game was won, else it return False and None
    @param board:
        board object
    @param player_obj:
        player object
    '''
    if board.check_win_vertically( player_obj ) == 3:
        return True, 'Vertically'

    if board.check_win_horizontally( player_obj ) == 3:
        return True, 'Horizontally'

    if board.check_win_left_to_right_diagonally( player_obj ) == 3:
        return True, 'Left to Right Diagonal'

    if board.check_win_right_to_left_diagonally( player_obj ) == 3:
        return True, 'Right to Left Diagonal'

    return False, None



def display_winner(board, player_obj, pattern):
    '''
    displays game winner and stops game play automatically
    @param board:
        represents the board object
    @param player_obj:
        represents the player object
    @param pattern:
        represents the pattern in which a player won the game
        can be 'Horizontal', 'Vertical', 'Diagonal'
    '''
    global gameFlag
    print(player_obj.playerName + f" wins the game --- { pattern }")

    gameFlag = False
    sys.exit(0)


def display_draw(  ):
    global gameFlag
    print("** ** Draw ** **")

    gameFlag = False
    sys.exit( 0 )


def compute_input_received( i_recieved, board_obj ):
    '''
    call appropriate method based on the input received
    '''

    # updates the current column position by moving it to the right and
    # re-display board
    if i_recieved.lower().startswith('r'):
        col_num = board_obj.move_column_to_right(i_recieved)
        row_num = board_obj.get_current_row( )
        display_top_info( )
        board_obj.set_rNc_position(col_num, row_num)


    # updates the current column position by moving it to the left and
    # re-display board
    if i_recieved.lower().startswith('l'):
        col_num = board_obj.move_column_to_left(i_recieved)
        row_num = board_obj.get_current_row( )
        display_top_info( )
        board_obj.set_rNc_position(col_num, row_num)


    # updates the current row position by moving it down and re-display board
    if i_recieved.lower().startswith('u'):
        col_num = board_obj.get_current_column( )
        row_num = board_obj.move_row_up(i_recieved )
        display_top_info( )
        board_obj.set_rNc_position(col_num, row_num)


    # updates the current row position by moving it down and re-display board
    if i_recieved.lower().startswith('d'):
        col_num = board_obj.get_current_column( )
        row_num = board_obj.move_row_down(i_recieved )
        display_top_info( )
        board_obj.set_rNc_position(col_num, row_num)


    # add player mark to current row and col position only if that position
    # has not been marked before. A user is given another chance to mark an
    # empty position in case mark was not placed

    if i_recieved.lower().startswith('m'):
        was_marked = False
        err_msg = ''
        playingPlayer = get_playing_player( )

        # only if a player still have move, then a player will be able to
        # mark a position
        was_marked = board_obj.mark_rNc_position(playingPlayer.playerMark)
        row_num = board_obj.get_current_row( )
        col_num = board_obj.get_current_column( )

        # only if the cell was marked then we want to reduce players
        # move count and also swap players turn
        if was_marked:
            board_obj.increment_num_of_board_marked( )

            # if there is a win
            won, winPattern = check_win( board_obj, playingPlayer)

            if won:
                display_top_info( )
                board.set_rNc_position(col_num, row_num)
                display_winner( board_obj, playingPlayer, winPattern)

            # if there is a draw
            if not won and board.get_num_board_marked( ) == 9:
                display_top_info( )
                board.set_rNc_position(col_num, row_num)
                display_draw( )


            # if there is no win swap players turn
            swap_player_turn( )


        display_top_info( )

        if len(err_msg) > 0:
            print(err_msg)
            board_obj.set_rNc_position(
                board_obj.get_current_column(), board_obj.get_current_row()
            )

        else:
            board_obj.set_rNc_position(col_num, row_num)





# ********************** Implementation of game engine ******************** #


# create players ( players can only be 2 )
for i in range(3):
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
