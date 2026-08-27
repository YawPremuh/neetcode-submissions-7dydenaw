class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for ch in strs:
            key = ''.join(sorted(ch))

            if key not in hash_map:
                hash_map[key] = []
            
            hash_map[key].append(ch)

        return list(hash_map.values())


            