class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for s in strs:
            key = ''.join(sorted(s))

            if key not in hash_map.keys():
                hash_map[key] = [s]
            else:
                hash_map[key].append(s)

        return list(hash_map.values())

