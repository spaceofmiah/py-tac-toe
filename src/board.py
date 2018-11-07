class Board:
    '''
    board presentative of game
    '''
    def __init__ ( self ):
        '''
        displays a tic tac toe board
        '''
        self._board = [
            [],[],[],
            [],[],[],
            [],[],[]
        ]
        self._drawBoard( )


    def _drawBoard( self ):
        '''
        doctype
        '''
        for row in range(len(self._board)):
            if row is not 0 and row % 3 == 0:
                print('|\n' + '|   '* 3 + '|')
            print("|***", end="")
        print('|\n' + '|   '* 3 + '|')
        print('|___'* 3 + "|")
