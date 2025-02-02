class Solution:
    def isPalindrome(self, x: int) -> bool:

        s = str(x)

        left, right, middle = 0, len(s)-1, len(s)//2

        if len(s) <= 0:
            return False
        elif len(s) == 1:
            return True
        else:
            for i in s[0:middle]:
                print(i)
                if i != s[right]:
                    print(i,right)
                    return False
                else:
                    left = left + 1
                    right = right - 1
            return True