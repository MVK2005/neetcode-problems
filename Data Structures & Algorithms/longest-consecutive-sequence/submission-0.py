class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        i = 0
        sorted_num = sorted(set(nums))
        n = len(sorted_num)
        result = 0
        curr, streak = sorted_num[0], 0
        while i < n:
            if curr != sorted_num[i]:
                curr = sorted_num[i]
                streak = 0
            while i < n and curr == sorted_num[i]:
                i+= 1
            streak += 1
            curr += 1
            result = max(streak, result)

        return result
                    
                
        
        