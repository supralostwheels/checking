#for analysing and manipulation of data,high performance
import pandas as pd

XYZ_web={"Day":[1,2,3,4,5,6],"Visitors":[1000,700,6000,1000,400,350],'Bounce Rate':[20,20,23,15,10,34]}
df=pd.DataFrame(XYZ_web)
print(df)

#slicing dataframe
print(df.head(2))
print(df.tail(2))

#merging->common rows and columns get merged
df1=pd.DataFrame({"HPI":[80,90,70,60],"Int_rate":[2,1,2,3],"IND_GDP":[50,45,4,56]},index=[2001,2002,2003,2004])
df2=pd.DataFrame({"HPI":[87,90,70,60,45],"Int_rate":[2,1,2,3,4],"IND_GDP":[50,45,4,56,34]},index=[2005,2006,2007,2008,2009])
merge=pd.merge(df1,df2)
print(merge)
merge1=pd.merge(df1,df2, on="HPI")
print(merge1)

#joining->new joined
df1=pd.DataFrame({"low_tier_HPI":[80,90,70,60],"Int_rate":[2,1,2,3],"IND_GDP":[50,45,4,56]},index=[2001,2002,2003,2004])
df2=pd.DataFrame({"HPI":[87,90,70,60,45]},index=[2005,2006,2007,
                                                                                                  2008,2001])
joined=df1.join(df2)
print(joined)
joined2=df2.join(df1)
print(joined2)


#changing index and column headers
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")
df=pd.DataFrame({"day":[1,2,3,4],"visitors":[200,300,400,500],"bounce_rate":[20,45,60,70]})
df.set_index("day",inplace=True)#inplace->Whether to modify the DataFrame rather than creating a new one.
print(df)
df.plot()
plt.show()

df=df.rename(columns={"visitors":"Users"})
print(df)


df1=pd.DataFrame({"HPI":[80,90,70,60],"Int_rate":[2,1,2,3],"IND_GDP":[50,45,4,56]},index=[2001,2002,2003,2004])
df2=pd.DataFrame({"HPI":[87,90,70,60,45],"Int_rate":[2,1,2,3,4],"IND_GDP":[50,45,4,56,34]},index=[2005,2006,2007,
                                                                                                  2008,2001])
Concat=pd.concat([df1,df2])
print(Concat)

#MUNGING->changing the format of the file
df=pd.read_csv("csvfile1.csv")
sb=df.to_html("csvfile1.html")
print(sb)
print(df)

df=df.head(5)
df=df.set_index(["Year"])
print(df)
sd=df.reindex(columns=['Total value','Value'])
print(type(sd))
sd=pd.DataFrame(sd)
print(type(sd))
sd['Total value'] = sd['Total value'].astype(int)
sd['Value'] = sd['Value'].astype(int)
print(sd.dtypes)
db=sd.diff(axis=1)
print(db)
db.plot(kind='bar')
plt.xlim()
plt.ylim()
plt.show()

