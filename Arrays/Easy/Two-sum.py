class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for index, value in enumerate(nums):
            remain = target - value

            if remain in seen:
                return [seen[remain], index]
            
            seen[value] = index
