class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            sortedstr = ''.join(sorted(i))
            res[sortedstr].append(i)
        return list(res.values())