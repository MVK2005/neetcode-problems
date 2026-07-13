class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        s_cleaned = ''.join((s_1.lower() for s_1 in s if s_1.isalnum()))

        start = 0
        end = len(s_cleaned) - 1
        for _ in range(len(s_cleaned)):
            while start <= end:
                if s_cleaned[start] != s_cleaned[end]:
                    return False
                start += 1
                end -= 1
        return True   


        