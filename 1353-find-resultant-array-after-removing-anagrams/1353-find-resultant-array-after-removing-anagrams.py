from collections import Counter
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        """
            Make an anagram helper
            1. start at idx 1, check back, if anagram, delete
            2. incr i
            3. repeat until end reached
        """

        def isAnagram(a, b):
            dictA = Counter(a)
            dictB = Counter(b)

            return dictA == dictB
        
        i = 1
        while i < len(words):
            if i > len(words):
                break
            
            if isAnagram(words[i], words[i - 1]):
                words.pop(i)
            else:
                i += 1

        return words
        