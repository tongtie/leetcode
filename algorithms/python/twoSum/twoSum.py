"""
// Source : https://leetcode.com/problems/two-sum/
// Author : Tong Tie
// Date   : 2021-05-18

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""
class Solution:
    # O(n2),自己写的
    def twoSumFirst(self, nums: List[int], target: int) -> List[int]:
        i, l = 0, len(nums) - 1
        j = l
        while i < l:
            if nums[i] + nums[j] == target:
                return i, j
            j -= 1
            if j <= i:
                j = l
                i += 1
    # O(n), 以空间换时间，保存有用的差值信息
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            if n in d:
                return [d[n], i]
            else:
                d[target - n] = i
