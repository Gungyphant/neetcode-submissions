import re

class Solution:
    reg = re.compile(r"([1-9][0-9]*)")
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        abbr_as_regex = self.reg.sub(r"[a-z]{\1}", abbr)
        return bool(re.fullmatch(abbr_as_regex, word))