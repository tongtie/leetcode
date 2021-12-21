# Merge Sort
## 归并排序

### Top-down Approach

自顶向下实现

![top-down](/images/explore/recursion-ii/divide-and-conquer/merge-sort-top-down.png)

#### 理解

* 拆分成只有一个或0个元素的子数组（1&2，拆分解决子问题）
* 对子数组两两排序合并，最终只剩一个有序数组

#### 实现

[Meger Sort by top down approach](merge_sort_top_down.py)


### 复杂度
先看原文解释，通俗易懂
![complexity](/images/explore/recursion-ii/divide-and-conquer/merge-sort-complexity.png)
#### 时间复杂度
1. 拆分。从上面的图1，我们知道将原始数组拆分成只包含一个元素的小数组的的步骤加起来总共是`o(N)`
2. 合并。还是上面的图1，从拆分完的数组（只包含一个元素）合并成有序的最终数组，需要反复进行`logN`次（即图中的`logN`层, 也就是3），每次需要N次比较，即总步骤为：`o(N*logN)`

#### 空间复杂度
是N，每次迭代都要有个长度为N的临时空间，保存当前迭代待排序的数组


### References
https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2868/


### 练习
https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2944/