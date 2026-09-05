class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        w = right - left
        h = min(heights[left], heights[right])
        res = h * w # max area ban đầu
        while (right - left) > 0:
            # cột nào nhỏ hơn thì dịch con trỏ vào trong
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
            h = min(heights[left], heights[right])
            if h * (right - left) > res:
                res = h * (right - left)
        return res