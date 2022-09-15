class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.isPalindrome(121))