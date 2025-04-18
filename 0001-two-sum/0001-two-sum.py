class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, value in enumerate(nums):
            y = target - value
            if y in seen:
                return [index, seen[y]]
            else:
                seen[value] = index






        