class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        number = 0

        for i in range(len(s)-1):  # 3
            if n[s[i + 1]] > n[s[i]]: #C>V, C<X, X>I
                number -= n[s[i]]   #-5
            else:
                number += n[s[i]]  # 95, 105,

        number += n[s[len(s) - 1]] #106
        return number



if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.romanToInt("VCXI"))