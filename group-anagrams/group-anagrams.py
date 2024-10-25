# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_map = defaultdict(list)

        if len(strs) == 0:
            return []

        for word in strs:
            key = ''.join(sorted(word))  # Use the sorted word as the key
            anagram_map[key].append(word)

        # Convert the values of the defaultdict to a list of lists
        return list(anagram_map.values())


        return 



        