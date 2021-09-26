""" A tic tac toe game. """

# standard modules
from argparse import ArgumentParser
import sys

# modules specific to this program
from board import Board
from player import HumanPlayer, ComputerPlayer


class TicTacToe:
    """ A tic tac toe game. Can be played by any humans and/or
    computers.
    
    Attributes:
        players (list of Player): the two players
        board (Board): the tic tac toe Board
        score (dict of Player: int): the players' scores
    """
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.score = {p: 0 for p in self.players}
        
    def reset_game(self):
        """ Switch the player's letters and order and get a new board.
        
        Side effects:
            Modifies self.board, self.players.
            Modifies each player's letter attribute.
        """
        self.board = Board()
        self.players.reverse()
        self.players[0].set_letter("x")
        self.players[1].set_letter("o")
        
    def play_round(self):
        """ Play one round of tic tac toe.
        
        Side effects:
            Writes to stdout.
            See also reset_game().
        """
        self.reset_game()
        for p in self.players:
            print(f"{p.name} is playing as {p.letter}")
            print()
        turn = 0
        while not self.board.game_over():
            player = self.players[turn % 2]
            player.take_turn(self.board)
            turn += 1

    def report_winner(self):
        """ Indicate who won the tic tac toe game.
        
        Side effects:
            Modifies self.score.
            Writes to stdout.
        """
        print()
        winner = self.board.get_winner()
        if winner:
            print(f"{winner.name} wins!")
            self.score[winner] += 1
        else:
            print("Tie game")
        for p in self.players:
            print(f"{p.name} has {self.score[p]} points")

    def play_game(self):
        """ Play multiple rounds of tic tac toe.
        
        Side effects:
            Writes to stdout.
            See also play_round(), report_winner().
        """
        while True:
            self.play_round()
            self.report_winner()
            while True:
                print()
                playagain = input("Play again? (y/n): ")
                if playagain == "n":
                    return    # end the whole method
                elif playagain == "y":
                    break     # just end the inner while statement
                print("Please type 'y' or 'n'")


def main(player1_name, player2_name):
    """ Create two Player objects and start a game of tic tac toe.
    
    Args:
        player1_name (str): the name of the first player. If the name
            is "computer", a computer player will be created. Otherwise,
            a human player will be created.
        player2_name (str): the name of the second player. If the name
            is "computer", a computer player will be created. Otherwise,
            a human player will be created.
    
    Side effects:
        Writes to stdout.
    """
    p1 = (ComputerPlayer("Rosie the Robot") if player1_name == "computer"
          else HumanPlayer(args.player1_name))
    p2 = (ComputerPlayer("Roger the Robot") if player2_name == "computer"
          else HumanPlayer(args.player2_name))
    game = TicTacToe(p1, p2)
    game.play_game()


def parse_args(arglist):
    """ Parse command line arguments.
    
    Arguments:
        arglist (list of str): a list of command-line arguments. Two
            arguments are expected (the names of the two players). The
            special value "computer" indicates that a computer player
            should be created. Any other value indicates that a human
            player should be created.
    """
    parser = ArgumentParser()
    parser.add_argument("player1_name", help="Player 1 name (or 'computer')")
    parser.add_argument("player2_name", help="Player 2 name (or 'computer')")
    args = parser.parse_args(arglist)
    return args


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.player1_name, args.player2_name)
