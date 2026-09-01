class Solution:
  def encode(self, strs: List[str]) -> str:
    res = []
    for s in strs:
      # Cấu trúc: [Độ dài] + '#' + [Nội dung chuỗi]
      res.append(f"{len(s)}#{s}")
    return "".join(res)

  def decode(self, s: str) -> List[str]:
    res = []
    i = 0

    while i < len(s):
      # Tìm vị trí ký tự '#' tiếp theo để lấy độ dài
      j = i
      while s[j] != "#":
        j += 1

      length = int(s[i:j])  # Chuyển độ dài từ string sang int
      i = j + 1  # Bỏ qua ký tự '#'

      # Lấy đúng số lượng ký tự theo 'length'
      res.append(s[i : i + length])

      i += length  # Nhảy đến từ tiếp theo

    return res