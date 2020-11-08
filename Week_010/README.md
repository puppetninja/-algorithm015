# Week10

## 数组、链表、跳表的实现

### 数组

数组的插入的复杂度为`O(N)`

### 链表

链表适合大量的插入删除操作

* 单链表
* 双链表
* 循环链表

链表的插入删除的复杂度为`O(1)`, 搜索为`O(N)`。

### 跳表 SkipList

有序的链表，并进行升维。实现简单，在项目中用来代替平衡二叉树

跳表的查询时间复杂度`O(N)`， 空间复杂度`O(logN)`

## 栈、队列、优先队列、双端队列

#### 栈和队列

##### 栈(Stack)

1. FILO
2. push `O(1)`
3. pop `O(1)`

##### 队列(Queue)

1. FIFO
2. push `O(1)`
3. pop `O(1)`

python `collections.deque`, `append(x)/appendleft(x)` and `pop()/popleft()`

Standard Python Library

collections ---> https://docs.python.org/3.8/library/collections.html

##### 优先队列(Priority Queue)

1. push `O(1)`
2. pop `O(logN)`, based on priority of elements

heapq ---> https://docs.python.org/3.8/library/heapq.html

## 哈希表

Map(dict in python)和 Set(set in python)底层都是通过Hash table来实现, 将关键码值映射到表中的值。

## 树、二叉树、二叉搜索树

树的通常解法都是递归

#### 二叉树最多只有两个子节点。

树的遍历：

* 前序遍历 `Preorder (Root, Left, Right) :根左右` 
* 中序遍历 `Inorder (Left, Root, Right) : 左根右`
* 后序遍历 `Postorder (Left, Right, Root) : 左右根`

#### 二叉搜索树:

* 左子树的所有节点值均小于根结点值
* 右子树的所有节点值均大于根结点值
* 以此类推，左右子树也为二叉查找树

二叉搜索树的中序遍历是升序排列

二叉搜索树查询和插入`O（logN`)

## 堆(Heap)和二叉堆(Binary Heap)

*Heap*: 可以迅速找到一堆数中的最大或者最小值的数据结构。

根结点最大的堆叫大顶堆或大根堆，最小的叫小顶堆或小根堆，常见的有二叉堆，Fibonacci Heap。

find-max: `O(1)`

delete-max: `O(logN)`

insert: `O(logN)` or `O(1)`

Python二叉堆实现: [heapq](https://docs.python.org/3.8/library/heapq.html)

heapq实现的最小二叉堆

```
heapq.heappush(heap, item)
Push the value item onto the heap, maintaining the heap invariant.

heapq.heappop(heap)
Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].

heapq.heappushpop(heap, item)
Push item on the heap, then pop and return the smallest item from the heap. The combined action runs more efficiently than heappush() followed by a separate call to heappop().

heapq.heapify(x)
Transform list x into a heap, in-place, in *linear* time.
```

Leetcode原题
leetcode-347: top k frequency elements
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

## Trie树-字典树

应用于词频感应

*优点*: 最大限度的减少无畏的字符串比较，查询效率比哈系表高

基本性质:

1. 结点本身不存完整单词
2. 从根节点到某一节点，路径上经过的字符连接起来，为该节点对应的字符串
3. 每个节点所有子节点路径代表的字符都不相同

核心思想：空间换时间， 利用字符串的公共前缀来降低查询时间的开销以达到提高效率的目的

代码模板

```python
# Python 
class Trie(object):
  
	def __init__(self): 
		self.root = {} 
		self.end_of_word = "#" 
 
	def insert(self, word): 
		node = self.root 
		for char in word: 
			node = node.setdefault(char, {}) 
		node[self.end_of_word] = self.end_of_word 
 
	def search(self, word): 
		node = self.root 
		for char in word: 
			if char not in node: 
				return False 
			node = node[char] 
		return self.end_of_word in node 
 
	def startsWith(self, prefix): 
		node = self.root 
		for char in prefix: 
			if char not in node: 
				return False 
			node = node[char] 
		return True
```



## 并查集

组团或配对问题

基本操作

1. makeSet(s): 建立一个新的并查集，包含s个单元素集合
2. unionSet(x, y): 把元素x和y所在的集合合并， 要求x和y所在的集合不相交， 如果相交则不合并
3. find(x): 找到元素x所在集合的代表， 该操作也可以用于i判断两个元素是否位于同一集合，只要将它们各自的代表比较一下就可以了

```python
# Python 
def init(p): 
	# for i = 0 .. n: p[i] = i; 
	p = [i for i in range(n)] 
 
def union(self, p, i, j): 
	p1 = self.parent(p, i) 
	p2 = self.parent(p, j) 
	p[p1] = p2 
 
def parent(self, p, i): 
	root = i 
	while p[root] != root: 
		root = p[root] 
	while p[i] != i: # 路径压缩 ?
		x = i; i = p[i]; p[x] = root 
	return root
```

## 高级搜索

### 初级搜索

1. 朴素搜索

2. 优化方式: 不重复(Fibonacci) 剪枝(生成括号问题)

3. 搜索方向: DFS/BFS

   双向搜索/启发式搜索 

### 剪枝

### 双向搜索

## AVL树和红黑树

极端情况二叉搜索树会变成链表

### 平衡二叉树

左右子树节点平衡（recursively）

1. 2-3 tree

2. AVL tree

3. B tree

4. Red Black tree

#### AVL数

平衡因子 Balance Factor: 左子树高度减去右子树高度， balance factor = {-1, 0, 1}

基于平衡因子

* 左旋

* 右旋

* 左右旋

* 右左旋

结点需要存储额外信息，且调整次数频繁

### 近似平衡二叉树

#### 红黑树

确保任何一个结点的左右子树的高度差小于两倍

* 节点 红或黑
* root/leave（NIL） 黑
* 不能有相邻接的两个红色节点
* 从任一节点到每个叶子的所有路径都包含相同数目的黑色节点

## 位运算

* 位运算符
* 算数移位与逻辑移位
* 位运算的应用

### 位运算符

左移 右移 或 与 取反 异或

## 布隆过滤器 Bloom Filter

#### Bloom Filter vs Hash Table

一个很长的二进制向量和一系列随机映射函数。布隆过滤器可以用于检索一个元素是否在一个集合中。

优点： 空间效率和查询时间都远远超过一般算法

缺点： 有一定的误识别率和删除困难

结论：如果元素不在，那么一定不在，如果存在，那么可能存在。

## LRU Cache 

示例代码

```python
# Python 

class LRUCache(object): 

	def __init__(self, capacity): 
		self.dic = collections.OrderedDict() 
		self.remain = capacity

	def get(self, key): 
		if key not in self.dic: 
			return -1 
		v = self.dic.pop(key) 
		self.dic[key] = v   # key as the newest one 
		return v 

	def put(self, key, value): 
		if key in self.dic: 
			self.dic.pop(key) 
		else: 
			if self.remain > 0: 
				self.remain -= 1 
			else:   # self.dic is full
				self.dic.popitem(last=False) 
		self.dic[key] = value
```



## 排序

### 常用高级排序

1. 快速排序 Quick Sort `O(nlogn)`
2. 归并排序 Merge Sort `O(nlogn)`
3. 堆排序 Heap Sort `O(nlogn)`, 堆插入`O(nlogn)`, 取最大最小值`O(1)`

总结：

1. 归并和快排具有相似性， 但步骤顺序相反

   归并： 先排序左右子数组， 然后合并两个有序子数组

   快排： 先调配出左右子数组，然后对于左右子数组进行排序

### 特殊排序

1. 计数排序 Counting Sort

   基于比较的排序算法， 将输入的数据值转化为键存储在额外开辟的数组空间中， 输入的数据必须在确定范围内的整数。

2. 桶排序 Bucket Sort

   利用函数的映射关系，假设输入数据服从均匀分布，将数据分到有限数量的桶里，每个桶再分别排序

3. 基数排序 Radix Sort

   按照低位排序，然后收集，再高位排序，然后收集，直到最高位。

## 字符串算法

字符串在java/python/go中都是immutable的。

在python中字符串iterable，直接遍历即可。

## 高级字符串算法

主要是通过动态规划和字符串操作相结合

通常是二维数组来计算两个字符之间的长度、回文等等

## 字符串匹配算法

1. 暴力法

2. Rabin-Karp算法

3. KMP算法

   

Rabin-Karp 算法

比较txt和pat的哈希值：

1. 不同必然不匹配
2. 相同朴素算法再次判断
