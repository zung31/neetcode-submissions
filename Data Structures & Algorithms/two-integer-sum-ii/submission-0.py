class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # ko dùng set được tại phải trả về index
        # nhưng dù gì thì hãy nhớ mảng đã được sort
        i = 0
        j = len(numbers) - 1
        while (numbers[i] + numbers[j]) != target:
            if numbers[i] + numbers[j] < target: # nhỏ hơn -> cần tăng i để tăng sum
                i += 1
            else: # lớn hơn -> cần giảm j để giảm sum
                j -= 1
        return [i + 1, j + 1]