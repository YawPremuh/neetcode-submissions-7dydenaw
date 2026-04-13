class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for s in strs:
            sorteds = ''.join(sorted(s))
            group[sorteds].append(s)
        return list(group.values())