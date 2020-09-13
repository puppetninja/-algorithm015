# Week03

## 递归的实现，特性以及思维要点

*树*的面试题解法一般都是递归

1. 节点的定义
2. 重复性（自相似性）

### 递归
递归的本质是循环，通过函数体进行的循环。

```python
# Python recursion template

def recursion(level, param1, param2):
    # recursion teminator 递归终结条件
    if level > MAX_LEVEL:
        process_result
        return

    # process logic in current level 处理当前层逻辑
    process(level, data)

    # drill down 下探到下一层
    self.recursion(level+1, p1, p2)

    # reverse the current elvel status if needed 清理当前层
```

思维要点

* 不要人肉递归
* 找到最近最简方法， 拆解成可重复解决的问题（重复子问题）
* 数学归纳法

Leetcode 原题：
1. Leetcode-22: 括号生成
2. Leetcode

### 分治，回溯
分治为一种特殊的递归

分治代码模板

```python
# Python
def divide_conquer(problem, param1, param2, ...):
  # recursion terminator
  if problem is None:
	print_result
	return

  # prepare data
  data = prepare_data(problem)
  subproblems = split_problem(problem, data)

  # conquer subproblems
  subresult1 = self.divide_conquer(subproblems[0], p1, ...)
  subresult2 = self.divide_conquer(subproblems[1], p1, ...)
  subresult3 = self.divide_conquer(subproblems[2], p1, ...)
  …

  # process and generate the final result
  result = process_result(subresult1, subresult2, subresult3, …)

  # reverse the current elvel status if needed 清理当前层
```

回溯-Backtracking
