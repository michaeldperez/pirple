class HangmanWord:
    def __init__(self, word):
        self.word = word
        self.obfuscated_word = self._obfuscate(word)
    
    def check(self, letter):
        if self._contains(self.word, letter):
            indices = self._find_indices(self.word, letter)
            self.obfuscated_word = self._reveal(letter, indices, self.obfuscated_word)
            if self._discovered(self.word, self.obfuscated_word):
                return (True, True)
            else:
                return (True, False)
        else:
            return (False, False)
    
    def _contains(self, word, letter):
        return (False, True)[letter in word]

    def _find_indices(self, word, letter):
        indices = []
        for index in range(len(word)):
            if word[index] == letter:
                indices.append(index)
        return indices
    
    def _obfuscate(self, word):
        obfuscated = ""
        for _ in range(len(word)):
            obfuscated += "_"
        return obfuscated
    
    def _reveal(self, letter, indices, obfuscated_word):
        obfuscated_word_list = list(obfuscated_word)
        for index in indices:
            obfuscated_word_list[index] = letter
        return ''.join(obfuscated_word_list)
    
    def _discovered(self, word, obfuscated_word):
        return word == obfuscated_word