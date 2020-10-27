# Week07

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
