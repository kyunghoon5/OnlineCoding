class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        out = ""
        for i in range(len(strs[0])):
            for j in strs:
                if i == len(j) or j[i] != strs[0][i]:
                    return out
            out += strs[0][i]
        return out

if __name__ == '__main__':
    # begin
    input_list = ["abc","abcd","abe"]
    s = Solution()
    print(s.longestCommonPrefix(input_list))