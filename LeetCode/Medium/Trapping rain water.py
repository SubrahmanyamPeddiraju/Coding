class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        for i in range(n):
            left_max = 0
            for j in range(i+1):
                left_max = max(left_max, height[j])
            right_max = 0
            for j in range(i, n):
                right_max = max(right_max, height[j])
            water += min(left_max, right_max) - height[i]
        return water
        
