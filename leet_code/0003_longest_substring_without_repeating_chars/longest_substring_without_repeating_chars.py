class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        solution = 0

        if len(s) <= 1:
            return len(s)

        for i,n in enumerate(s):
            window = []
            window.append(n)
            for j,m in enumerate(s[i+1:]):
                if m not in window:
                    window.append(m) 
                    window_size = len(window)
                    if window_size > solution:
                        solution = window_size
                else:
                    window_size = len(window)
                    if window_size > solution:
                        solution = window_size
                    break

        return solution
