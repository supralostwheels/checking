"""COLLECTIONS IN PYTHON"""
#CONTAINER DATATYPES->LISTS,TUPLES,SETS,DICTIONARY
#COLLECTIONS MODULES->SPECIALIZED DATA STRUCTURES->
#1.NAMEDTUPLE()->TO DISCARD THE LIMITATIONS OF TUPLE TO REMEMBER INDEXES
from collections import namedtuple,deque,ChainMap,Counter,OrderedDict,defaultdict
a=namedtuple('courses','name,technology')
s=a('artificial intelligence','python')
d=a._make(['artificial intelligence','python'])  #by using list
print(s,"\n",d)

#2.DEQUE()->OPTIMISED LIST TO PERFORM INSERTION AND DELETION EASILY(P.A->DECK)
a=[1,2,3,4,5,6]
d=deque(a)
print(d) 
d.appendleft(8)
print(d)
d.popleft()
print(d)

#3.CHAINMAP()->DICTIONARY LIKE CLASS FOR CREATING A SINGLE VIEW OF MULTIPLE MAPPINGS
a = {1: 'edureka', 2: 'python'}
b ={3: 'ML', 4: 'AI'}
a1= ChainMap(a,b)
print(a1)

#4.COUNTER()->DICTIONARY SUBCLASS FOR COUNTING HASHABLE OBJECTS
a=[1,1,2,3,4,3,3,2,3,2]
c=Counter(a)
print(c)
print(list(c.elements()))
print(c.most_common())
sub={2:1,6:1}
print(c.subtract(sub))
print(c.most_common())


#5.OrderedDict->DIctionary subclass which remembers the order in which the entries were done
d=OrderedDict()
d[1]=1
d[2]=2
d[3]=3
d[4]=4
d[5]=5
d[6]=6
print(d)
d[1]=5
print(d)

#6.defaultdict->dictionary subclass which calls a factory function to supply missing values
d=defaultdict(int)
d[1]='python'
d[2]='eudreka'

print(d[3])      #gives no error

#7.UserDict,UserList,UseString-A wrapper around dictionary/List/String objects for easier dictionary sub-classing

