#Introduction->Used for data visualization.,complex visualizations
#why not matplotlib->working with dataframes easier,more customizable themes
#dependencies->numpy,scipy,matplotlib,pandas,statsmodel

"""Visualizaing statistical relationships"""#->relationships of variables with one another
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# for scattered plotting
# a=sns.load_dataset("flights")    #we can check the github repo for the datasets
# x=sns.relplot(x="passengers",y="month",data=a)    #2-D
# # plt.show()
#
# a=sns.load_dataset("flights")    #we can check the github repo for the datasets
# x=sns.relplot(x="passengers",y="month",hue="year",data=a)    #3-D
# # plt.show()
#
# #for line plotting
# a=sns.load_dataset("flights")    #we can check the github repo for the datasets
# x=sns.relplot(x="passengers",y="month",data=a,kind="line")    #2-D
# # plt.show()
#
"""PLOTTING CATEGORICAL DATA"""
# a=sns.load_dataset("tips")
# sns.catplot(x="day",y="total_bill",data=a)
# # plt.show()
#
# a=sns.load_dataset("tips")
# sns.catplot(x="day",y="total_bill",data=a,kind="box")
# # plt.show()
#
#
"""VISUALIZE DATASETS DISTRIBUTUION"""
# #plotting univariate distributions->Univariate distribution is a statistical data series that shows the frequency of a single variable
# c=np.random.normal(loc=5,size=100,scale=2)
# sns.displot(c)
#
# #plotting bivariate distributions->, while bivariate distribution shows the frequency of two variables at the same time.
# df = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [6, 7, 8, 9, 10]})
# sns.jointplot(x='x', y='y', data=df)
# # plt.show()
#
# a=sns.load_dataset("iris")
# b=sns.FacetGrid(a,col='species')
# b.map(plt.hist,"sepal_length")
# # plt.show()
#
# a=sns.load_dataset('flights')
# b=sns.PairGrid(a)
# b.map(plt.scatter)
# # plt.show()

"""CUSTOMIZATIONS"""
# sns.set(style="white",color_codes=True)
# a=sns.load_dataset('tips')
# sns.boxplot(x="day",y="total_bill",data=a)
# plt.show()

#remove axes
# sns.set(style="white",color_codes=True)
# a=sns.load_dataset('tips')
# sns.boxplot(x="day",y="total_bill",data=a)
# sns.despine(offset=10,trim=True)
# plt.show()


#color pallete
c=sns.color_palette()
sns.palplot(c)
plt.show()

