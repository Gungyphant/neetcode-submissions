import re

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        abbr_as_regex = re.sub(r"([1-9][0-9]*)", r"[a-z]{\1}", abbr)
        print(abbr_as_regex)
        return bool(re.fullmatch(abbr_as_regex, word))