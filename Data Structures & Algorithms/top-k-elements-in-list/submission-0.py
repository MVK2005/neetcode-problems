from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_freq = Counter(nums)
        top_k = nums_freq.most_common(k)
        result = [s[0] for s in top_k]
        return list(result)