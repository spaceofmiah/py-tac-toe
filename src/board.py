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


        # set board key navigation characters
        # r -- Right { column navigation }     d -- Down { row navigation }
        # l -- Left  { column navigation }     u -- Up   { row navigation }
        self._board_nav_char = ["r", "l", "d", "u"]


        # mark position
        self.colMark = 4


        # current position row-wise and column-wise
        self._curRow = 1
        self._curCol = 1


        # displays the board at the second column and second row by default
        mvColRight = self.move_column_to_right('r')
        mvRowDown = self.move_row_down('d')

        self.set_rNc_position( mvColRight, mvRowDown)


        # displays the board at the first column and third row by default
        mvColRight = self.move_column_to_left('l')
        mvRowDown = self.move_row_down('d')

        self.set_rNc_position( mvColRight, mvRowDown)


    def _drawBoard( self, rowNum ):
        '''
        PRIVATE METHOD
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





    def set_rNc_position( self, colNum, rowNum ):
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
        PRIVATE METHOD
        sets a mark at the current position within board interface

        @param rowNum:
            the desired row number in which mark will be placed representing
            the current row
        '''
        print(" " * (self.colMark * self._curCol - 2) + "C")
        self._drawBoard( rowNum )





    def _mark_row_position_on_board( self, count, rowNum ):
        '''
        PRIVATE METHOD
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
        PRIVATE METHOD
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



    def move_column_to_right(self, right):
        '''
        changes the current position of the column by incrementing it by one.
        incrementing column by one moves it to the right.
        @param right:
                this is char `r` which represents right
        returns an incremented column number or same column number ( only
        in the case where column number is at it's peak which is 3 )
        '''
        rightMv = self._validate_rNc_movement_input(right)
        if rightMv.lower() == "r":
            # if the current column number is not 3 yet, then will the
            # current column be incremented by one
            if self._curCol != 3:
                self._curCol += 1
                return self._curCol

        return self._curCol



    def move_column_to_left(self, left):
        '''
        changes the current position of the column by decrementing it by one.
        decrementing column by one moves it to the left.
        @param left:
                this is char `l` which represents left
        returns a decremented column number or same column number ( only
        in the case where column number is at it's base which is 1 ).
        '''
        leftMv = self._validate_rNc_movement_input(left)
        if leftMv.lower() == "l":
            # if the current column number is not 1 yet, then will the
            # current column be decremented by one
            if self._curCol != 1:
                self._curCol -= 1
                return self._curCol

        return self._curCol



    def move_row_down(self, down):
        '''
        changes the current position of row by incrementing it by one.
        incrementing row by one moves it down.
        @param down:
                this is char `d` which represents down
        returns an incremented row number or same row number ( only
        in the case where row number is at it's peak which is 3 ).
        '''
        mvDown = self._validate_rNc_movement_input(down)
        if mvDown.lower() == "d":
            # if the current row number is not 3 yet, then will the
            # current row be incremented by one
            if self._curRow != 3:
                self._curRow += 1
                return self._curRow

        return self._curRow



    def move_row_up(self, up):
        '''
        changes the current position of row by decrementing it by one.
        decrementing row by one moves it up.
        @param down:
                this is char `u` which represents up
        returns a decremented row number or same row number ( only
        in the case where row number is at it's base which is 1 ).
        '''
        mvUp = self._validate_rNc_movement_input(up)
        if mvUp.lower() == "u":
            # if the current row number is not 3 yet, then will the
            # current row be incremented by one
            if self._curRow != 1:
                self._curRow -= 1
                return self._curRow

        return self._curRow




    def _validate_rNc_movement_input(self, mvInput):
        '''
        PRIVATE METHOD
        this checks the movement input inserted by the user if it is present
        in the defined movement characters.
        movement characters can only be:
            `r` -- Right { column navigation }
            `d` -- Down { row navigation }
            `l` -- Left  { column navigation }
            `u` -- Up   { row navigation }
        if and invalid movement character is entered an error is returned else
        the input character is returned
        '''
        mvInput = str(mvInput)

        # should in case a user mistakenly insert more than one character
        if len(mvInput) > 1:
            mvInput = list(mvInput)[0]

        if mvInput.lower() in self._board_nav_char:
            return mvInput

        else:
            raise Exception(
                f"InputError: {mvInput} not an valid navigation character")
