class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        vowels=0
        consonants=0
        vowels_set="aeiouAEIOU"
        for c in word:
            if c.isalpha():
                if c in vowels_set:
                    vowels+=1
                else:
                    consonants+=1
            elif not c.isdigit():
                return False
        return vowels>=1 and consonants>=1