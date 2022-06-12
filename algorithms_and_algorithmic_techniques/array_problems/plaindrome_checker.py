def isPalindrome(s):
    class Solution:
        def isPalindrome(self, s: str) -> bool:
            s = convertedString(s)
            l = 0
            r = len(s) - 1

            while l < r:
                if s[l] != s[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            return True

    def convertedString(s):
        s2 = s.lower()
        s3 = s2.replace(" ", "")
        s4 = ''.join(ch for ch in s3 if ch.isalnum())
        return s4


