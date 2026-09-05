class Solution:

  def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()  # 1. Sort mảng để dùng Two Pointers: O(N log N)
    res = []
    n = len(nums)

    for i in range(n - 2):
      # Bỏ qua phần tử trùng lặp cho 'i' để tránh kết quả bị trùng
      if i > 0 and nums[i] == nums[i - 1]:
        continue

      # Nếu số nhỏ nhất > 0 thì tổng 3 số không thể bằng 0 được nữa
      if nums[i] > 0:
        break

      # 2. Hai con trỏ Two Pointers cho phần mảng còn lại
      left = i + 1
      right = n - 1

      while left < right:
        total = nums[i] + nums[left] + nums[right]

        if total == 0:
          res.append([nums[i], nums[left], nums[right]])

          # Bỏ qua các giá trị trùng lặp của left và right
          while left < right and nums[left] == nums[left + 1]:
            left += 1
          while left < right and nums[right] == nums[right - 1]:
            right -= 1

          left += 1
          right -= 1
        elif total < 0:
          left += 1  # Cần tăng tổng lên
        else:
          right -= 1  # Cần giảm tổng xuống

    return res