class Board:
    '''
    board presentative of game
    '''
    def __init__ ( self ):
        '''
        Tic Tac Toe board constructor
        '''
        # sets the structure of board
        self._board = [
            [],[],[],
            [],[],[],
            [],[],[]
        ]

        # mark position
        self.colMark = 4
        self.rowMark = 3


        # current position row-wise and column-wise
        self._curRow = 1
        self._curCol = 1


        # displays the board at the first column by default
        self._setColumnPosMark( 1 )


    def _drawBoard( self ):
        '''
        draws tic tac toe board UI
        '''
        for row in range(len(self._board)):

            if row is not 0 and row % 3 == 0:
                print('|\n' + '|   '* 3 + '|')

            print("|***", end="")

        print('|\n' + '|   '* 3 + '|')
        print('|___'* 3 + "|")



    def _setColumnPosMark( self, colNum ):
        '''
        sets the column position on board interface.
        current column position is identified with `C` a mark
        @param colNum:
            colNum is the desired column number a user chooses to work on
        '''
        # validate passed column
        self._curCol = self._validate_columnn_number(colNum)

        # mark and drawboard
        self._mark_position_and_draw_board(  )



    def _mark_position_and_draw_board(self):
        '''
        sets a mark at the current position within board interface
        '''
        print(" " * (self.colMark * self._curCol - 2) + "C")
        self._drawBoard( )




    def _validate_columnn_number( self, colNum ):
        '''
        validate column number, making sure it's not greater than 3 and
        lesser than 1
        @param colNum:
                colNum is a numeric value that shouldn't be greater than
                3 and lesser than 1
        '''
        if colNum > 3:
            return 3
        if colNum < 1:
            return 1
        return colNum
