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
找realmid的位置：

参考：https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14425/Concise-O(log-N)-Binary-search-solution

For those who struggled to figure out why it is realmid=(mid+rot)%n: you can think of it this way:
If we want to find realmid for array [4,5,6,7,0,1,2], 
you can shift the part before the rotating point to the end of the array (after 2) so that the sorted array is "recovered" from the rotating point but only longer, 
like this: [4, 5, 6, 7, 0, 1, 2, 4, 5, 6, 7]. The real mid in this longer array is the middle point between the rotating point and the last element: 
(rot + (hi+rot)) / 2. (hi + rot) is the index of the last element. And of course, this result is larger than the real middle. 
So you just need to wrap around and get the remainder: ((rot + (hi + rot)) / 2) % n. And this expression is effectively (rot + hi/2) % n, which is (rot+mid) % n.
Hope it helps!

### 翻译过来：

先上概念：

原始数组为A： [0, 1, 2, 4, 5, 6, 7]

旋转数组为B：[4, 5, 6, 7, 0, 1, 2]

旋转点k为: 3 (1 <= k < nums.length), 对应数组中的值为4 (0-indexed)

rot： 可以理解为旋转部分的长度，即nums.length - k

realmid： 是原始数组的中间值的坐标

mid： 是当前数组的中间坐标(代表一个中间的位置，对应的值不一定是当前数组的中间值)

n： 是数组的长度

hi： 是当前数组的最大坐标, 即: n - 1

我们可以通过以下公式求出realmid, 思路如下：

realmid = (mid + rot) % n

我们将旋转数组中的前rot个元素移动到数组的末尾，这样数组变为了：[4, 5, 6, 7, 0, 1, 2, 4, 5, 6, 7]， 我们暂且叫它数组L。

在数组L中求realmid的位置即： (rot + (hi + rot)) / 2, 因为realmid的位置在rot和最后一个元素之间，也就是数组L的4th和10th之间（0-indexed）

(hi + rot)是数组L的最后一个元素的索引。当然，这个结果比实际的中间值大。

所以你只需要绕一圈，得到余数: (rot + (hi + rot)) / 2) % n。

把上面的表达式简化下为：(rot+ hi/2) % n，也就是(rot + mid) % n。

"""

"""
解决思路：

    我们通过2分查找要找到target，就要找到realmid

    那么我们只要在数组A中找到关键的点即可。关键点是：最小值、最大值、中间值或者旋转点。

    假如我们找最小值，最小值一定在数组A的左半部、中间或右半部。我们用2分查找数组A，用mid和hi对应的值去比较就可以找到。

    我们知道了最小值，就可以知道其他的关键点了，比如rot。

    这样，我们在后面的2分查找target时，就可以求得每次迭代中，当前数组的realmid。（通过(rot + mid) % n），注意mid和realmid每次迭代中都是变化的）

    注：求target的这个2分查找，可以这样理解： rot + mid即数组L中的realmid， mid的对应的值没用，主要使用他的坐标，用于找realmid，最后用realmid对应的值和target比较

"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1
        # lo = hi, 最小值的坐标
        rot = lo
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            realmid = (mid + rot) % len(nums)
            if nums[realmid] == target:
                return realmid
            elif nums[realmid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2,3] # nums.length = 8
    nums = [4,5,0,1,2] # 5
    nums = [0,1,2,3,4] # 5
    nums = [1,2,3,4,5,0] # 6
    target = 0
    print(Solution().search(nums, target))
