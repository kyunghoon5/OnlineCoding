class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = True
        while start:
            if '()' in s:
                s = s.replace('()','')
            elif '[]' in s:
                s = s.replace('[]','')
            elif '{}' in s:
                s = s.replace('{}','')
            else:
                start = False

        return True if len(s) == 0 else False





if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.isValid('[]'))