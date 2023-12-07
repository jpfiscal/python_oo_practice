"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    
    def __init__(self,word_file):
        self.word_list = self.read_in_file(word_file)
        

    def read_in_file(self, word_file):
        word_list_builder = []
        file = open(word_file)
        for line in file:
            word_list_builder.append(line.strip())
        print(f"{len(word_list_builder)} words read")
        return word_list_builder

    def random(self):
        return self.word_list.pop(random.randint(0,len(self.word_list)-1))

class SpecialWordFinder(WordFinder):
    """Specialized Word Finder which excludes blank lines as well as anything that starts with '#'

    >>> swf = SpecialWordFinder("word_test.txt")
    15 words read

    >>> swf.random() in ["Black beans", "Pinto beans", "Chickpeas", "Chicken breast", "Protein powder", "Fish", "Choy", "Spinach", "Kale", "Avocado"]
    True

    >>> swf.random() in ["Black beans", "Pinto beans", "Chickpeas", "Chicken breast", "Protein powder", "Fish", "Choy", "Spinach", "Kale", "Avocado"]
    True

    >>> swf.random() in ["Black beans", "Pinto beans", "Chickpeas", "Chicken breast", "Protein powder", "Fish", "Choy", "Spinach", "Kale", "Avocado"]
    True
    """
    def __init__(self, word_file):
        super().__init__(word_file)

    def Random(self):
        valid_string = False
        while valid_string == False:
            random_index = random.randint(0,len(self.word_list)-1)
            random_word = self.word_list[random_index]
            if len(random_word) > 0 and random_word.startswith('#') == False:
                valid_string == True
                return self.word_list.pop(random_index)
                