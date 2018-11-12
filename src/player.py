class Player:
    '''
    Player representation of game
    '''

    def __init__(self, playerNum, playerName):
        '''
        player constructor
        @param playerNum ( integer ):
            represent the player's number
        @param playerName ( string ):
            represent the player's name
        '''

        # player's name
        self.playerName = playerName

        # represents a player's mark on board
        self.playerMark = 'p' + str(playerNum)

        # represents the amount of move a player can make
        self.moveCount = 3



    def reduce_player_move(self):
        '''
        reduces player's move
        '''
        if self.moveCount != 0:
            self.moveCount -= 1



    def increase_player_move(self):
        '''
        increases player's move
        '''
        if self.moveCount != 3:
            self.moveCount += 1
