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

![证明是二叉查找树1](images/explore/recursion-ii/divide-and-conquer/DC-template-validate-BST-1.png)
![证明是二叉查找树2](images/explore/recursion-ii/divide-and-conquer/DC-template-validate-BST-2.png)

递归过程中，终止的条件是: 只包含一个根节点的树或空树都是二叉查找树。

[python示例](/algorithms/python/validate-binary-search-tree/validate-binary-search-tree.py)

### References
https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2869/

