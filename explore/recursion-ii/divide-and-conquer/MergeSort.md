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

### References
https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2868/