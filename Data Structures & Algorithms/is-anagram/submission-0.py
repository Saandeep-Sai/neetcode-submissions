class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = True
        s_occurances = {}
        t_occurances = {}
        if len(s) != len(t):
            return False
        for i in s:
            s_occurances[i] = s_occurances.get(i,0)+1
        for i in t:
            t_occurances[i] = t_occurances.get(i,0)+1
        for i in s:
            if s_occurances.get(i) != t_occurances.get(i):
                anagram = False
                break
        return anagram 