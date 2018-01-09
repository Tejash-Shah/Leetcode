class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if (word.islower()==True or word.isupper()==True or word.istitle()==True):
            return True
        else:
            return False
        