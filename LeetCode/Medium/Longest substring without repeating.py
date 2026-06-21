class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        char_index = {}
        left = 0
        maxLen = 0
        for right in range(n):
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1
            char_index[s[right]] = right
            maxLen = max(maxLen, right - left + 1)
        return maxLen
        
