class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, num_zeroes = 1, 0

        for num in nums:
            if num:
                prod *= num
            else:
                num_zeroes += 1

        if num_zeroes > 1:
            return [0] * len(nums)
        
        result = [0] * len(nums)

        for i, c in enumerate(nums):
            if num_zeroes:
                result[i] = 0 if c else prod
            else:
                result[i] = prod//c
        return result

            
        