# Divide and Conquer template
解决分而治之问题的模版，分而治之的问题都可以往模版里面套

## 模版
![分而治之解决问题模版](/images/explore/recursion-ii/divide-and-conquer/DC-template.png)

伪代码

```python
def divide_and_conquer( S ):
    # (1). Divide the problem into a set of subproblems.
    [S1, S2, ... Sn] = divide(S)

    # (2). Solve the subproblem recursively,
    #   obtain the results of subproblems as [R1, R2... Rn].
    rets = [divide_and_conquer(Si) for Si in [S1, S2, ... Sn]]
    [R1, R2,... Rn] = rets

    # (3). combine the results from the subproblems.
    #   and return the combined result.
    return combine([R1, R2,... Rn])
```

### 示例
#### Validate Binary Search Tree
证明一棵树是二叉查找树
1. 递归拆分问题成子问题（子问题和原始问题是不是同一个问题。这里左子树和右子树都是二叉查找树）
2. 解决问题（如何验证是二叉查找树）
3. 合并子问题的解，生成最终解。（即左子树是二叉查找树、右子树也是二叉查找树，并且合并起来也满足二叉查找树的性质）

![证明是二叉查找树1](/images/explore/recursion-ii/divide-and-conquer/DC-template-validate-BST-1.png)
![证明是二叉查找树2](/images/explore/recursion-ii/divide-and-conquer/DC-template-validate-BST-2.png)

递归过程中，终止的条件是: 只包含一个根节点的树或空树都是二叉查找树。

[python示例](/algorithms/python/validate-binary-search-tree/validate-binary-search-tree.py)

#### Search a 2D Matrix II
判断一个值是否在2维数组中，此2维数组有如下性质：
* 从左到右升序排列
* 从上到下升序排列

根据上面的性质，我们知道，任意切割此矩阵，得到的子矩阵也满足如上性质。那么此问题就可以套用分而治之模版解决。

* Divide. 可以找一个中间点（行和列的中间点），将矩阵切割成4个子矩阵。
* Conquer. 递归的从这4个子矩阵寻找target
* Combine. 只要从任意一个子矩阵找到target, 则返回成功

注： 当矩阵是空时，或只包含一个元素时，则返回（只有子元素相等时返回True，否则返回False)。

![2维有序矩阵查找数据](/images/explore/recursion-ii/divide-and-conquer/DC-template-search-2d-matrix-II-1.png)

##### 改进-只需要查询3个子矩阵

我们知道矩阵是有序的
* 当分割点等于target时，返回True
* 当分割点小于target时，我们可以舍弃左上部分子矩阵，因为它里面的值都小于分割点的值
* 当分割点大于target时，我们可以舍弃右下部分子矩阵，因为它里面的值都大于分割点的值

![2维有序矩阵查找数据只需要查询3个子矩阵](/images/explore/recursion-ii/divide-and-conquer/DC-template-search-2d-matrix-II-2.png)

##### 改进-只需要查询2个子矩阵

我们如果能找到这样一个点，V(i,j)， 其中i是行，j是列。

当满足V(i, j) < target 同时 V(i + 1, j) > target时， 

我们只要继续在V(i, j)点的右上部分子矩阵和V(i + 1, j)点的左下部分子矩阵中查询target即可。

![2维有序矩阵查找数据只需要查询2个子矩阵](/images/explore/recursion-ii/divide-and-conquer/DC-template-search-2d-matrix-II-3.png)

[python示例](/algorithms/python/search-a-2d-matrix-ii/search-a-2d-matrix-ii.py)


### References
https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2869/

