#Joseph Sanchez
#Shima Abdulla
#Sydney Small
from board import Board

class LoggingBoard(Board):
    """ A subclass of the board class that records important events throughout the tictactoe game.
    """
    def __init__(self):
        """ Creates a list called clog where the logging info is eventually to be held
        """
        super().__init__()
        self.log = []
        
    def claim_square(self,player,index):
        """ Overides the clas square method so one person can claim the square and this info is in the log. Has arguements of Player and index.
        """
        super().claim_square(player,index)
        self.log.append(f"{player.name} selects square {index}")
    
    def get_winner(self):
        """ Puts the winners name in the log. Arguement would be if their is a winner. Returns the winner
        """
        winner = super().get_winner()
        if winner == True:
            self.log.append(f"{winner.name} wins")
        return winner
    
    def game_over(self):
        """ Puts the result of the game in the log by overider the game_over method and eventuallly storing the results. Arguements within the code is that if their is a result it would print out the result and. This eventuallty would return the results of the game.
        """
        game_result = super().game_over()
        if game_result == True:
            for i in self.log:
                print (i)
        return game_result