#Names(Me, Partner 1, Partner 2): Shima Abdulla, Sean Delaney, Wenchen Wang
class Match:
    
    def __init__(self,date, opponent, home, md_score, other_score):
        """ Initializes the date, opponent, home, md_score, other_score, and home"""
        self.date = date
        self.opponent = opponent
        self.home = home
        self.md_score = md_score
        self.other_score = other_score
        
    def win(self):
        """ Determines if Maryland won or loss the game using the md_score and other_score variable and returns a boolean value (True for win False for lose)"""
        return self.md_score > self.other_score
    
def read_scores(file_name):
    """ reads the file and creates an instance of class for the scores in the file. Creates list that stores a results of each match to the file
    Args: filename
    Return: a results list with the results of each game"""
    with open(file_name, "r", encoding = "utf-8") as f:

        result = []
        for line in f:
            line = line.rstrip()
            values = line.split("|")
        
            val = Match(date = values[0],
                opponent = values[2],
                home = (values[1] == "home"),
                md_score = int(values[3]),
                other_score = int(values[4])
                )
            
            result.append(val)
            
    return result
    
    