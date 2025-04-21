class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for str in strs:
            str_sorted_tuple = tuple(sorted(str))

            if str_sorted_tuple in anagrams:
                anagrams[str_sorted_tuple].append(str)
            else:
                anagrams[str_sorted_tuple] = [str]

        return list(anagrams.values())