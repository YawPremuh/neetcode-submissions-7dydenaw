class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        groups = {}

        for s in strs:
            key = ''.join(sorted(s))
            if key not in groups.keys():
                groups[key] = [s]
            else:
                groups[key].append(s)

        return list(groups.values())

