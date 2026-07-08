from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums_freq = Counter(nums)

        for key,value in nums_freq.items():
            if nums_freq[key] > 1:
                return True

        return False

        