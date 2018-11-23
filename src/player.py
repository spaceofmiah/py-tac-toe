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
