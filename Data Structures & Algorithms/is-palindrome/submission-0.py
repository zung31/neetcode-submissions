class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Chỉ giữ lại chữ/số và chuyển về chữ thường
        clean_s = "".join(ch.lower() for ch in s if ch.isalnum())

        # 2. So sánh với chuỗi đảo ngược
        return clean_s == clean_s[::-1]