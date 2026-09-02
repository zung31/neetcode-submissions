class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i < j:
            # ko if dc vì có thể 2 kí tự ko hợp lệ cạnh nhau
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower(): # phải cùng case nx 
                return False
            i += 1
            j -= 1
        return True 