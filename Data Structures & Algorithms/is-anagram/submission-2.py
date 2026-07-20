class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Hs = Counter(s)
        Ht = Counter(t)
        return Hs == Ht