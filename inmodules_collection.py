from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter

#namedtuple可以创建坐标，圆圈等  而不用重新建立类 

Point=namedtuple('Point',['x','y'])
p=Point(1,2)
print(p.x)
print(p.y)
print(isinstance(p,Point))
print(isinstance(p,tuple))


#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈,deque除了实现list的append()和pop()外，还支持appendleft()和popleft()
#这样就可以非常高效地往头部添加或删除元素。

q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)


#使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：

dd=defaultdict(lambda:'N/A')
dd['key1']='abc'
print(dd['key1'])
print(dd['key2'])


#使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
#如果要保持Key的顺序，可以用OrderedDict
#OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：

d=dict([('a',1),('b',2),('c',3)])
print(d)

od=OrderedDict([('a',1),('b',2),('c',3)]
)
print(od)


#Counter是一个简单的计数器，例如，统计字符出现的个数：

c=Counter()
for ch in 'love xiaomengmeng~':
	c[ch]=c[ch]+1

print(c)

