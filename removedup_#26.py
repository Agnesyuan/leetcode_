# -*- coding: utf-8 -*-
"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
[1, 1, 2]--> 2 ; [0, 0, 1, 1, 2, 3, 3, 4] --> 5
"""
class Solution:

    def removeDuplicates(self, nums):

        # 第一种方法 正向遍历 超出时间限制
        # n = len(nums)
        # for i in range(n-1):
        #     if nums[i] == nums[i+1]:
        #         nums.pop(i)
        #         return self.removeDuplicates(nums)
        # return nums
        #return len(nums)

        # 反向遍历
        for i in range(len(nums)-1, 0, -1):
            if nums[i] == nums[i-1]:
                nums.pop(i)
        return nums

        #  不需要pop数据，生成最后的数组，只需遍历数组 记录元素个数即可
        # if len(nums) <= 1:
        #     return len(nums)
        # s = 0
        # for i in range(1, len(nums)):
        #     if nums[s] != nums[i]:
        #         s += 1
        #     nums[s] = nums[i]
        # return s + 1

if __name__ == '__main__':
    s = Solution()
    nums = [0, 0, 1, 1, 2, 3, 3, 4]
    print(s.removeDuplicates(nums))

# a = [1, 3, 9, 4, 5]
# for i in range(2, len(a)):
#     print(i)
#     a.pop(i)
#     break
# print(a)
