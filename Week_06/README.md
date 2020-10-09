# Week06

## 动态规划

前情回顾：

1. 人肉递归低效、很累
2. 找到最近最简方法，将其拆解成可重复解决问题
3. 数学归纳法思维

本质： 寻找重复性 --》 计算机指令集

### 动态规划

定义

https://en.wikipedia.org/wiki/Dynamic_programming

Divide & Conquer + Optimal substructure (分治 + 最优子结构)

#### 关键点

* 动态规划和递归或者分治没有根本上的区别（关键看有无最优解）
* 共性： 找重复子问题
* 差异性： 最优子结构、中途可以淘汰次优解

#### 例题

1. Fibonacci数列, 一维

   * 傻递归
   * 带记忆性的搜索, memoization`O(n)`
   * Bottom up, 尾递归

2. Count the path， 二维

   * 状态转移方程（DP方程）

     ```
     opt[i, j] = opt[i+1, j] + opt[i, j+1]
     ```

### 动态规划关键点

1. 最优子结构 `opt[n]=best_of(opt[n-1], opt[n-2]....)`
2. 存储中间状态 `op[i]`
3. 递推公式（状态转移方程或者DP方程）

#### MIT 5 steps of DP

1. define subproblems
2. guess (part of solutions)
3. relate subproblem solutions
4. recurse and memoization
5. solve original problem
