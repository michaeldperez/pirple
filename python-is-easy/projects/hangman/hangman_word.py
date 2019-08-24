class HangmanWord:
    def __init__(self, word):
        self.word = word
    
    def check(self, letter):
        if self._contains(self.word, letter):
            return self._find_indices(self.word, letter)
        else:
            return None
    
    def _contains(self, word, letter):
        return (False, True)[letter in word]

    def _find_indices(self, word, letter):
        indices = []
        for index in range(len(word)):
            if word[index] == letter:
                indices.append(index)
        return indices