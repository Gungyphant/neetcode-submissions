import re

class WordDictionary:

    def __init__(self):
        self.words = set()
        

    def addWord(self, word: str) -> None:
        self.words.add(word)
        

    def search(self, word: str) -> bool:
        return any(re.fullmatch(word, known_word) for known_word in self.words)
