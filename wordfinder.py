from random import randint
import os
"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """Machine that reads file, finds list of words, and finds number of words on list.
    
    >>> wf = WordFinder("~/student/words.txt")
    3 words read
    
    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self, filepath):
        """Opens file with file_path and file_name"""
        if not (filepath):
            raise AttributeError("Please enter both file_path and file_name resepctively.")
        self.filepath = filepath
        self.words_list = self.collect_words()
        print(f"{len(self.words_list)} words read")

    def collect_words(self):
        """Reads file and makes list of the words on file."""
        file = open(os.path.expanduser(self.filepath))
        lst = [line.strip() for line in file]
        file.close()
        return lst

    def random(self):
        """Returns a random word from list of words in .txt file."""
        return self.words_list[randint(0,len(self.words_list)-1)]
    



