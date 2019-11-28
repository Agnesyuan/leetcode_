# -*- coding: utf-8 -*-
"""
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
"""
class Solution:

    def removeElement(self, nums, val):
        # 执行用时 48ms，内存消耗 13.5MB
        s = 0
        n = len(nums)
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
                s += 1
        return nums,  n - s


if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 2, 3]
    print(s.removeElement(nums, 3))