class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char_occurences = {}
        t_char_occurences = {}
        for c in s:
            if c not in s_char_occurences:
                s_char_occurences[c] = 0
            s_char_occurences[c] += 1
        for c in t:
            if c not in t_char_occurences:
                t_char_occurences[c] = 0
            t_char_occurences[c] += 1
        
        print(s_char_occurences, t_char_occurences)
        return s_char_occurences == t_char_occurences
        



