# -*- coding: utf-8 -*-
"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

"""
class Solution:

    def twoSum(self, nums, target):
        # 第一种方法 索引 执行用时 1064ms，内存消耗 14.6MB
        # for i in range(len(nums)):
        #     a = target - nums[i]
        #     if a in nums and nums.index(a) != i:
        #         return i, nums.index(a)

        # 第二种方法 字典 执行用时 84ms，内存消耗 15.2MB
        d = {}
        for i in range(len(nums)):
            a = target - nums[i]
            if nums[i] in d:
                return d[nums[i]], i
            else:
                d[a] = i


if __name__ == '__main__':
    s = Solution()
    nums = [2, 11, 7, 15]
    target = 9
    print(s.twoSum(nums, target))