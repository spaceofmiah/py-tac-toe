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

        # current position row-wise and column-wise
        self._curRow = 1
        self._curCol = 1


        # displays the board at the first column and first row by default
        self._set_rNc_position( self._curCol, self._curRow)


    def _drawBoard( self, rowNum ):
        '''
        draws tic tac toe board UI
        '''
        count = 0

        # validate row number
        self._curRow = self._validate_rNc_number(rowNum)

        for row in range(len(self._board)):

            if row is not 0 and row % 3 == 0:
                count += 1
                print('|\n' + '|   ' * 3 +
                      f'''| {
                               self._mark_row_position_on_board(
                                   count, self._curRow
                                 )
                            }'''
                     )


            print("|***", end="")

        print('|\n' + '|   ' * 3 +
              f'''| {
                       self._mark_row_position_on_board(
                           3, self._curRow
                         )
                    }'''
             )

        print('|___'* 3 + "|")





    def _set_rNc_position( self, colNum, rowNum ):
        '''
        sets row and column position on board interface.
        current column position is identified with `C` mark while
        current row position is identified with `R` mark

        @param colNum:
            colNum is the desired column number a user chooses to work on

        @param rowNum:
            rowNum is the desired row number a user chooses to work on
        '''
        # validate passed column
        self._curCol = self._validate_rNc_number(colNum)

        # mark and drawboard
        self._mark_column_position_and_draw_board( rowNum )






    def _mark_column_position_and_draw_board(self, rowNum):
        '''
        sets a mark at the current position within board interface

        @param rowNum:
            the desired row number in which mark will be placed representing
            the current row
        '''
        print(" " * (self.colMark * self._curCol - 2) + "C")
        self._drawBoard( rowNum )





    def _mark_row_position_on_board( self, count, rowNum ):
        '''
        determines when row mark is to be placed
        @param count, rowNum:
            count:
                count helps to tell the amount of times that we have
                created a row only when the amount of cells % 3 is equal to 0
            rowNum:
                the desired position we wish to place our row mark row number
                cannot be greater than three and cannot be lesser than 1

        will return a mark `R (row)` in the right row choosen
        '''
        if rowNum == 1 and count == 1:
            return " R"

        if rowNum == 2 and count == 2:
            return " R"

        if rowNum == 3 and count == 3:
            return" R"
        return ""





    def _validate_rNc_number( self, colNum ):
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
