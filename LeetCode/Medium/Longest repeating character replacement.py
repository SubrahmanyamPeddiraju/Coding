class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        l = 0 
        r = 0
        maxFreq = 0
        hm = {}
        while r < len(s):
            hm[s[r]] = hm.get(s[r], 0) + 1
            maxFreq = max(maxFreq, hm[s[r]])
            while ((r - l + 1) - maxFreq )> k:
                hm[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
            r += 1
        return maxLen
