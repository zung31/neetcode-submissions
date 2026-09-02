class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for num in num_set: # set ko truy cập dc bằng index
            if (num - 1) in num_set: # nếu tồn tại value nhỏ hơn nó 1 đv
                continue # suy ra không phải điểm bắt đầu   
            l_sub = 1 # coi như len sub -> sau phải + 1?
            while (num + l_sub) in num_set:
                l_sub += 1
            if res < l_sub:
                res = l_sub
        
        return res