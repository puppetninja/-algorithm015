# Week04

## 深度优先/广度优先的实现和特性

遍历搜索
在树（图/状态集）中寻找特定节点

* 每个节点都要访问一次
* 每个节点仅仅访问一次


对于节点的访问顺序不限

* 深度优先: DFS deep first search
* 广度优先: BFS breadth first search

优先级优先搜索，用于推荐系统

### 深度优先 DFS

```python
# 二叉树的遍历
def dfs(node):
    if node is visited:
        return

    visited.add(node)

    # Process current node
    # .... # Logic here

    dfs(node.left)
    dfs(node.right)
```

```python
# DFS 代码 - 递归写法
visited = set()

def dfs(node, visited):
    visited.add(node)
    # process current node

    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node, visited)

```

### 广度优先 BFS

使用队列

```python
def bfs(graph, start, end):L
    queue = []
    queue.append([start])
    visited.add(start)

    while queue:
        node = queue.pop()
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)

    # other processing work
```

## 贪心算法 Greedy

贪心算法是一种在每一步选择中都选取当前状态最好或是最优的选择， 从而导致结果是全局最好或是最优的算法。

贪心算法与动态规划的不同在于对每个子问题的解决方案都作出选择， 不能回退。动态规划会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。

* 贪心：当下做局部最优判断
* 回溯：能够回退
* 动态规划：最优判断 + 回退

贪心算法一般不能得到所要求的答案，一旦一个问题可以通过贪心来解决，那么贪心是解决的最好办法。由于贪心算法的高效性，可以用作辅助算法来解决精度要求不高的问题。

## 二分查找

二分查找一定是有序的，不然只能便利。

1. 目标函数单调性(单调递增或者递减)
2. 存在上下界(bounded)
3. 能够通过索引访问(index accessible)

```python
left,right = 0, len(array)-1
while left <= right:
	mid = (left + right) / 2
    if array[mid] == target:
        # find the target!!
        break or return result
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

