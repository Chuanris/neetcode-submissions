class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ik = {}
        ij = {}
        for i in s:
            ik[i] = ik.get(i, 0) + 1
        for j in t:
            ij[j] = ij.get(j, 0) + 1

        if ij == ik:
            return True
        else:
            return False
