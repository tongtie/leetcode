# Quick Sort

Quick Sort 也是一种分而治之类型的排序算法，由英国科学家Tony Hoare在1959提出。
如果实现的好的话，他比其他的排序算法如归并排序能快2，3倍，这就是它为什么叫快排。

TODO: 能否实现一种这样的？

## 介绍

解决分而治之类算法的三个步骤：
1. 分解问题，变成多个子问题
2. 解决子问题
3. 合并子问题的解

### 快排算法
1. 在待排序数组中，找一个基准点(pivot)，将数组分成两个子数组，左边的子数组`小于`基准点，右边的子数组`大于等于`基准点。
这个过程也叫做分割(partitioning)。找基准点的方法有很多种，最简单的就是取第一个元素或随机取数组中的一个元素。
2. 重复步骤1，递归的求解分割后的两个子数组。
3. 当子数组是空或只包含一个元素时，停止递归。从左到右，任意一个左边子数组中的元素都小于它右边子数组中的元素。
最终只要把这些子数组，追加到一块，整体数组即是有序数组。

快排的核心算法是分割的过程，每次分割都向着最终有序又近了一步。

![quick sort intuition](/images/explore/recursion-ii/divide-and-conquer/quick-sort-intuition.png)

## 算法图解

如下图所示，pivot取的是最后一个元素，递归分割子问题，最终得到有序数组

![quick sort algorithm](/images/explore/recursion-ii/divide-and-conquer/quick-sort-algorithm.png)

## 算法示例

```python
def quicksort(lst):
    """
    Sorts an array in the ascending order in O(n log n) time
    :param nums: a list of numbers
    :return: the sorted list
    """
    n = len(lst)
    qsort(lst, 0, n - 1)

def qsort(lst, lo, hi):
    """
    Helper
    :param lst: the list to sort
    :param lo:  the index of the first element in the list
    :param hi:  the index of the last element in the list
    :return: the sorted list
    """
    if lo < hi:
        p = partition(lst, lo, hi)
        qsort(lst, lo, p - 1)
        qsort(lst, p + 1, hi)

def partition(lst, lo, hi):
    """
    Picks the last element hi as a pivot
     and returns the index of pivot value in the sorted array
    """
    pivot = lst[hi]
    i = lo
    for j in range(lo, hi):
        if lst[j] < pivot:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
    lst[i], lst[hi] = lst[hi], lst[i]
    return i

```

## 时间复杂度

由于分割方式的不同，时间复杂度在最好O(Nlog2^N)和最坏O(N^2)之间，N是数组长度。

通过数学方法证明，时间复杂度为O(Nlog2^N)


### 最好
每次取的pivot都正好可以将数组平分，也就是一颗平衡二叉搜索树(balanced binary search tree)。
树的高度是log2^N（也就是经过log2^N次切割，子数组是空或只包含一个元素的数组)。
树的每层都要做一次比对（分割的过程）O(N)次，
所以是O(Nlog2^N)

### 最坏
每次取的pivot都是待排序数组的最大或最小的点，这样每次分割成一个空的子数组和一个包含剩余元素的子数组(除去pivot)。
即时间复杂度为：N + N-1 + N-2 + ... + 1， 即求和公式为：N(N+1)/2, 即O(N^2)
在这种情况下，快排就变成了插入排序了。

![quick sort complexity](/images/explore/recursion-ii/divide-and-conquer/quick-sort-complexity.png)


## References
https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2870/