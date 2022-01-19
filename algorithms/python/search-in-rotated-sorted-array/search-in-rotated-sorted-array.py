"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 

such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 

For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4


Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1



Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-10^4 <= target <= 10^4
"""
"""
参考：https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14425/Concise-O(log-N)-Binary-search-solution

For those who struggled to figure out why it is realmid=(mid+rot)%n: you can think of it this way:
If we want to find realmid for array [4,5,6,7,0,1,2], 
you can shift the part before the rotating point to the end of the array (after 2) so that the sorted array is "recovered" from the rotating point but only longer, 
like this: [4, 5, 6, 7, 0, 1, 2, 4, 5, 6, 7]. The real mid in this longer array is the middle point between the rotating point and the last element: 
(rot + (hi+rot)) / 2. (hi + rot) is the index of the last element. And of course, this result is larger than the real middle. 
So you just need to wrap around and get the remainder: ((rot + (hi + rot)) / 2) % n. And this expression is effectively (rot + hi/2) % n, which is (rot+mid) % n.
Hope it helps!

对于那些努力弄明白为什么它是realmid=(mid+rot)%n的人:你可以这样想:

如果我们想找到realmid阵列(4、5、6、7 0,1,2),你可以旋转点前的一部分转移到数组的末尾(2)之后,这样排序数组的“恢复”旋转点但只有长,像这样:(4、5、6、7 0,1,2,4,5,6,7]。在这个较长的数组中，真正的中间点是旋转点和最后一个元素(rot + (hi+rot)) / 2之间的中间点。(hi + rot)是最后一个元素的索引。当然，这个结果比实际的中间值大。所以你只需要绕一圈，得到余数:(rot+ (hi + rot)) /2) % n。这个表达式是有效的(rot+ hi/2) % n，也就是(rot+mid) % n。

希望它可以帮助!
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[lo] < nums[hi]:
                hi = mid
            else:
                lo = mid
