class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #Method 1
        return sorted(s) == sorted(t)

        #Method 2
        return Counter(s) == Counter(t)
        