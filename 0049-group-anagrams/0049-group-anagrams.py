class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = {}

        for str in strs:
            str_sorted_tuple = tuple(sorted(str))

            if str_sorted_tuple in memo:
                memo[str_sorted_tuple].append(str)
            else:
                memo[str_sorted_tuple] = [str]

        return list(memo.values())