from wordfinder import WordFinder
import os

class SpecialWordFinder(WordFinder):
    """WordFinder, but ignores blank lines and comments.
    >>> swf = SpecialWordFinder("newwords.txt")
    4 words read
    
    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True
    """

    def collect_words(self):
        lst = []
        file = open(os.path.expanduser(self.filepath))
        for line in file:
            l = line.strip()
            if l and not '#' in l:
                lst.append(l)
        file.close()
        return lst
    
    