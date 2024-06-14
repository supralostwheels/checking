#TYPE OF DATA STRUCTURE THAT MAPS KEYS TO ITS VALUE PAIRS
#Example->Use Dictionaries->curly braces or dict function


#Using curly braces
mydict={'Dave':'hello','jas':'idk'}
print(mydict)
mydict2=dict(Dave='hello',jas='idk')
print(mydict2)

"""NESTED DICTIONARIES"""
emp_details={'Employee':{'Dave':{'id':'001','Department':'Sales'},
                         'JAS':{'id':'002','Department':'TECH'}}}
print(emp_details)


"""ACCESSING VALUES"""
#Using key values
print(mydict['Dave'])
print(mydict.get('Dave'))
print(mydict.keys())
print(mydict.values())
for x,y in mydict.items():
    print(x,y)

"""UPDATING VALUES"""
mydict['Dave']='004'
mydict['Chris']='001'
print(mydict)

"""DELETING VALUES"""
mydict.pop('Chris')
print(mydict)
print(mydict.popitem())
del mydict['Dave']
print(mydict)


"""DICT TO DF"""
import pandas as pd  #Pandas is a Python library used for working with data sets
df=pd.DataFrame(emp_details['Employee'])
print(df)