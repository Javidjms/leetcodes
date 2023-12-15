class Solution:
    def longestCommonPrefix(self, strings: List[str]) -> str:
      current_prefix = ""
      long_set = set()
      max_long_count = 0
      for elements in zip(*strings):
        if all(e == elements[0]for e in elements):
          current_prefix += elements[0]
          if len(current_prefix) > max_long_count:
            long_set.add(current_prefix)
            max_long_count = len(current_prefix)
        else:
          break
      return max(long_set) if len(long_set) else ""
      