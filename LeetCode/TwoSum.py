class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return[i, j]

if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))