class Solution:

  def trap(self, height: List[int]) -> int:
    n = len(height)
    if n == 0:
      return 0

    # 1. Tính Suffix Max (Max từ phải sang trái)
    suffix_max = [0] * n
    suffix_max[-1] = height[-1]
    for i in range(n - 2, -1, -1):
      suffix_max[i] = max(height[i], suffix_max[i + 1])

    # 2. Duyệt từ trái sang phải, vừa duy trì Prefix Max vừa tính nước
    prefix_max = 0
    res = 0

    for i in range(n):
      prefix_max = max(prefix_max, height[i])

      # Mực nước tối đa tại vị trí i được quyết định bởi cột thấp hơn trong 2 bờ
      water_level = min(prefix_max, suffix_max[i])
      res += water_level - height[i]

    return res