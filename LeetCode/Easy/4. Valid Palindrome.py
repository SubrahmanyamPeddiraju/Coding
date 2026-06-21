class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = ''
        s = s.lower()
        for char in s:
            if char.isalnum():
                l += char
        return l == l[::-1]
