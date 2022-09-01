"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
"""
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 第k大的数转换成第nums.length - k + 1小的数（因为是升序排列）
        k = len(nums) - k  + 1  
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = self.partition(nums, left, right)
            if pivot == k - 1:
                return nums[pivot]
            elif pivot < k - 1:
                left = pivot + 1
            else:
                right = pivot - 1
        return nums[left]
    
    def partition(self, nums, left, right):
        import random
        pivot = random.randint(left, right)
        nums[pivot], nums[right] = nums[right], nums[pivot]
        pivot = right
        i = left
        for j in range(left, right):
            if nums[j] < nums[pivot]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[pivot] = nums[pivot], nums[i]
        return i
