# Week08

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
