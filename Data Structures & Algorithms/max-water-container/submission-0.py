class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        local_area = 0
        Area = []
        while left<right:
            local_area = min(heights[left],heights[right])*abs((left-right))
            Area.append(local_area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max(Area)

        