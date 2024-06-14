#human brain processes information easily when it picturizes data
#quickly interprets the data and selection of important variables
#matplotlib is a python package used for 2D graphics
#BAR,HISTOGRAMS,SCATTERPLOT

from matplotlib import pyplot as plt
# plt.plot([1,2,3],[4,5,1])
# plt.show()
#
# x=[5,8,10]
# y=[12,16,6]
# plt.plot(x,y)
# plt.title("info")
# plt.ylabel("yaxis")
# plt.xlabel("xaxis")
# plt.show()
#
# from matplotlib import style
# style.use("ggplot")
# x=[5,8,10]
# y=[12,16,6]
# x2=[6,9,11]
# y2=[6,15,7]
# plt.plot(x,y,"g",label='lineone',linewidth=5)
# plt.plot(x2,y2,"c",label='linetwo',linewidth=5)
# plt.title("info")
# plt.ylabel("y-axis")
# plt.xlabel("x-axis")
# plt.legend()
# plt.grid(True,color='k')
# plt.show()



"""BAR"""
# plt.bar([1,3,5,7,9],[5,2,7,8,2],label="Example one",color='r')
# plt.bar([2,3,6,8,9],[1,2,3,4,5],label="Example two",color='g')
# plt.legend()
# plt.xlabel("bar number")
# plt.ylabel("bar height")
# plt.title('Bar graph')
# plt.show()

# """HISTOGRAM"""
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Generate random data for the histogram
# data = np.random.randn(1000)
#
# # Plotting a basic histogram
# plt.hist(data, bins=30, color='skyblue', edgecolor='black')
#
# # Adding labels and title
# plt.xlabel('Values')
# plt.ylabel('Frequency')
# plt.title('Basic Histogram')
#
# # Display the plot
# plt.show()

"""SCATTERPLOT"""
# import matplotlib.pyplot as plt
# x=[1,2,3,4,5,6,7,8]
# y=[5,2,4,2,1,4,5,2]
# plt.scatter(x,y,label='skitscat',color='k')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Scatter')
# plt.legend()
# plt.show()


"""STACKPLOT"""#->AREA PLOT ->similar to a line graph only difference being the area under the line is shaded so as
# to show a trend
# import matplotlib.pyplot as plt
# days=[1,2,3,4,5]
# sleeping=[7,8,6,11,7]
# eating=[2,3,4,3,2]
# working=[7,8,7,2,2]
# playing=[8,5,7,8,13]
#
# plt.plot([],[],color='m',label='Sleeping',linewidth=5)
# plt.plot([],[],color='c',label='Eating',linewidth=5)
# plt.plot([],[],color='r',label='Working',linewidth=5)
# plt.plot([],[],color='k',label='Playing',linewidth=5)
#
# plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','k'])
#
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Area Plot')
# plt.legend()
# plt.show()

"""PIE CHART"""
# import matplotlib.pyplot as plt
# slices=[7,2,2,13]#slices are basically sizes correspondingly
# activities=['sleeping','eating','working','playing']
# cols=['c','m','b','r']
# plt.pie(slices,labels=activities,colors=cols,startangle=90,shadow=True,explode=(0,0.1,0,0),autopct="%1.1f%%")    #0.1
# # for the slice you want to stand out , autopct ->to write the percentages
# plt.title('Pie Plot')
# plt.show()


"""HANDLING MULTIPLE PLOTS"""
import numpy as np
import matplotlib.pyplot as plt
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1=np.arange(0.0,5.0,0.1)
t2=np.arange(0.0,5.0,0.02)
plt.subplot(212)    #(212)->2 graphs 1 horizontally and print the second plotting first
plt.plot(t1,f(t1),'bo')#first plotting

plt.subplot(211)
plt.plot(t2,np.cos(2*np.pi*t2))#second plotting
plt.show()





