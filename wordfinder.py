"""Word Finder: finds random words from a dictionary."""
""" Picking a random word from words.txt document"""

"""
    Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
"""


import random

class WordFinder:
    def __init__(self, file):
        self.file = file
        """Open the file in read mode""" 
        text_file = open(file)
        """file.read reads all of the words in the document"""
        self.words = self.find(text_file)
        print(f"{len(self.words)} words read")
     
                  

    """The attribute of the number of the list of the words that was read"""
    def find(self, text_file):
        """
        the process to the list of words using text_file
        """
        print[open("words.txt","r").readline().split()]


    def random(self):
        """Print random word"""
        print(random.choice(self.words)) 

class SpecialWordFinder(WordFinder):
    def find(self, text_file):
            print[open("complex.txt","r").readline().split()]
            
        

"""https://docs.python.org/3/library/collections.html#collections.Counter"""
"""https://www.youtube.com/watch?v=_mjZjpOmN0k&ab_channel=AiCore"""
"""https://www.youtube.com/watch?v=mNpCPgdb2Jg&ab_channel=PythonandPandaswithReuvenLerner"""

       
        

