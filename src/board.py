from colr import color


class Board:
    '''
    board representation of game
    '''
    def __init__ ( self ):
        '''
        Tic Tac Toe board constructor
        '''
        # sets the structure of board
        self._board = [
            ["np", "np", "np"],
            ["np", "np", "np"],
            ["np", "np", "np"],
        ]


        # set board key navigation characters
        # r -- Right { column navigation }     d -- Down { row navigation }
        # l -- Left  { column navigation }     u -- Up   { row navigation }
        self._board_nav_char = ["r", "l", "d", "u"]


        self._game_won_count = 0
        self._num_of_board_marked = 0


        # mark position
        self.colMark = 7


        # current position row-wise and column-wise
        self._current_row = 1
        self._current_column = 1


        # by default when a board is drawn it set the
        # row at position 1 and set the column at position 1
        self.set_rNc_position(self._current_row, self._current_column)



    def _drawBoard( self, rowNum ):
        '''
        PRIVATE METHOD
        draws tic tac toe board UI
        '''
        rowCount = 1

        # validate row number
        self._current_row = self._validate_rNc_number(rowNum)

        for row in self._board:
          print("----------------------")

          for col in row:
              print("|  " + col, end="  ")

          print(
            f"| { self._set_row_position_on_board(rowCount, self._current_row)}"
          ) # end of a row

          rowCount += 1

        print("----------------------")





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
        self._current_column = self._validate_rNc_number(colNum)

        # mark and drawboard
        self._set_column_position_and_draw_board( rowNum )






    def _set_column_position_and_draw_board(self, rowNum):
        '''
        PRIVATE METHOD
        sets a mark at the current position within board interface

        @param rowNum:
            the desired row number in which mark will be placed representing
            the current row
        '''
        print(" " * (self.colMark * self._current_column - 4) + "C")
        self._drawBoard( rowNum )





    def _set_row_position_on_board( self, count, rowNum ):
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
            # if the current column number is not yet 3, only then will the
            # current column be incremented by one
            if self._current_column != 3:
                self._current_column += 1
                return self._current_column

        return self._current_column




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
            if self._current_column != 1:
                self._current_column -= 1
                return self._current_column

        return self._current_column




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
            if self._current_row != 3:
                self._current_row += 1
                return self._current_row

        return self._current_row




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
            if self._current_row != 1:
                self._current_row -= 1
                return self._current_row

        return self._current_row





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




    def mark_rNc_position(self, marker):
        '''
        helps to mark current position if no mark is already present
        returns True if mark was successfully placed else returns False
        '''
        new_mark = self._validate_marker(marker)
        can_mark_position = self._check_mark_presence()

        # give different color to different player's mark symbol
        if new_mark == "p1":
            new_mark = color(new_mark, fore="red")
        else:
            new_mark = color(new_mark, fore="blue")

        # curRow and curCol doesn't start from 0 and our list is 0 indexed
        # whenever curRow and curCol is not 0 we will always subtract 1

        if self._current_row != 0 and self._current_column != 0:
            if can_mark_position:
                self._board[self._current_row-1].pop(self._current_column-1)
                self._board[self._current_row-1].insert(self._current_column-1, new_mark)
                return True

        else:
            if can_mark_position:
                self._board[self._current_row].pop(self._current_column)
                self._board[self._current_row].insert(self._current_column, new_mark)
                return True

        return False



    def _validate_marker(self, marker):
        '''
        validates the length of marker. marker is to be 2 characters long
        '''
        if len(marker) > 2:
            # convert to string and to list
            marker = list(str(marker))

            # return the first two element
            return ''.join(marker[:2])

        return marker


    def _check_mark_presence(self):
        '''
        PRIVATE METHOD
        helps to validate if a user can mark current row and column position
        in board. returns true if user can mark else it returns false
        '''

        # _current_row and _current_column doesn't start from 0 and our list is 0 indexed
        # whenever _current_row and _current_column is not 0 we will always subtract 1

        if self._current_row > 0 and self._current_column > 0:
            result = self._board[self._current_row-1][self._current_column-1].strip()
        else:
            result = self._board[self._current_row][self._current_column].strip()
        if result != "np":
            return False
        return True



    def get_current_row(self):
        '''
        returns the current row
        '''
        return self._current_row




    def get_current_column(self):
        '''
        returns the current column
        '''
        return self._current_column




    def check_win_vertically( self, playerObj ):
        '''
        checks if there is a win vertically. A win can only be determined only if
        there is an occurence ( thrice ) of a particular player's mark
        in identical columns.
        return the number of count calculated
        '''
        # to iterate vertically on a matrix, the column will be fixed and the row
        # will increment

        # we use matrix to draw table, whose count begins from 0
        # so whatever the current column is, we'll subtract one.
        column_num = self._current_column-1
        for i in range(3):

            # self._board[i][column_num] will not return the player mark on a column,
            # but instead it will return the building blocks of that column
            # including the player's mark, column bars( | ) and spaces.

            if  playerObj.playerMark in self._board[i][column_num]:
                self._game_won_count += 1
            else:
                self._game_won_count = 0
        print("game won count --> ", self._game_won_count)
        return self._game_won_count



    def check_win_horizontally(self, playerObj):
        '''
        checks if there is a win horizontally. A win can only be determined only if
        there is an occurence ( thrice ) of a particular player's mark in
        rows.
        returns the number of count calculated
        '''
        # to iterate horizontally on a matrix, the row will be fixed and the column
        # will increment

        row_num = self._current_row - 1
        for i in range(3):

            # self._board[row_num][i] will not return the player mark on a row,
            # but instead it will return the building blocks of that row
            # including the player's mark, column bars( | ) and spaces.

            if playerObj.playerMark in self._board[row_num][i]:
                self._game_won_count += 1
            else:
                self._game_won_count = 0
                break

        return self._game_won_count



    def check_win_left_to_right_diagonally(self, playerObj):
        '''
        checks if there is a win diagonally(left to right). A win can only be
        determined only if there is an occurence ( thrice ) of a particular
        player's mark in rows.
        returns the number of count calculated
        '''
        # to iterate diagonally (left to right) on a matrix, the row and the  
        # column will have increment together. At first increment, position
        # will be at row 1 column 1, and at second increment, position will
        # be at row 2 column 2 e.t.c ( it is the column that actually count in the
        # row of a matrix )

        for i in range(3):
            if playerObj.playerMark in self._board[i][i]:
                self._game_won_count += 1

            else:
                self._game_won_count = 0
                break

        return self._game_won_count




    def check_win_right_to_left_diagonally(self, playerObj):
        '''
        checks if there is a win diagonally(right to left). A win can only be
        determined only if there is an occurence ( thrice ) of a particular
        player's mark in rows.
        returns the number of count calculated
        '''
        # to iterate diagonally (right to left) on a matrix, the row and the  
        # column will have decrement together.

        for i in range(3):
            # our matrix is 3 x 3 but multi-dimensional array in python starts
            # it's counting from 0, so in the real sense our matrix is 2 x 2
            # (0 becomes 1).
            #
            # self._board[i][(2-i)]
            # simply means, the current row(i), and column ( 2 - i ::: 
            # if i is 0, then 2-0) ( 2 is the total number of column of matrix
            # in 0th base ), which will literally makes our column count start
            # from the right side of the matrix

            if playerObj.playerMark in self._board[i][(2-i)]:
                self._game_won_count += 1

            else:
                self._game_won_count = 0
                break

        return self._game_won_count


    def increment_num_of_board_marked( self ):
        '''
        '''
        self._num_of_board_marked += 1


    def get_num_board_marked( self ):
        '''
        '''
        return self._num_of_board_marked
