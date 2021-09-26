#Names: Shima Abdulla, Wenchen Wang, Varun Sharma

import re

def get_words(s):
    """ Extract a list of words from string s.

    Args:
        s (str): a string containing one or more words.

    Returns:
        list of str: a list of words from s converted to lower-case.
    """
    words = list()
    s = re.sub(r"--+", " ", s)
    for word in re.findall(r"[\w'-]+", s):
        word = word.strip("'-_")
        if len(word) > 0:
            words.append(word.lower())
    return words

class UniqueWords:
    """ Determines unique words in a given file after determining the set of words that are unique to a file takes the init method, the add_file method and the unique method"""
    def __init__(self):
        """ Iniitializes variables for all words, unique words and words in the file"""
        self.all_words = set()
        self.unique_words = set()
        self.words_by_file = {}
        
    def add_file(self, file_name, key):
        """ Determines the differnet words between the unique words set and the words in the file as well as the  
        by using the words in those specifc stes and dictionaries creates a new_words list with the different words between the file and all the words"""
        with open(file_name, "r", encoding = "utf-8") as f:
            files = f.read()
            self.words_by_file[key] = set(get_words(files))
        
        self.unique_words= self.unique_words - (self.words_by_file[key])
        new_words = self.words_by_file[key] - (self.all_words)
        self.unique_words.update(new_words)
        self.all_words.update(new_words)
        
    def unique(self, key):
        """ Function returns the unique words by using the similarities in the unique words set ad the all words set"""
        return self.unique_words.intersection(self.all_words)
            
            
        
    
 