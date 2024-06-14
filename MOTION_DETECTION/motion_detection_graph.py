# The final step in our use-case to display the results. We are displaying the graph which denotes the motion on 2-axes. Consider the below code:
# To begin with, we import the DataFrame from the motion_detector.py file.
# The next step involves converting time to a readable string format which can be parsed.
# Lastly, the DataFrame of time values is plotted on the browser using Bokeh plots.


from Motion_detection_using_open_cv import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource
import pandas as pd
df['Start']=pd.to_datetime(df['Start'])
df['End']=pd.to_datetime(df['End'])

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)       #cds now has the column names as df

p = figure(x_axis_type='datetime', height=100, width=500, title="Motion Graph")
# p.yaxis.minor_tick_line_color = None
# p.ygrid[0].ticker.desired_num_ticks = 1

hover = HoverTool(tooltips=[("Start", "@Start_string"), ("End", "@End_string")])
p.add_tools(hover)

q = p.quad(left="Start", right="End", bottom=0, top=1, color="green", source=cds)
#The quad() function in Bokeh is used to draw axis-aligned rectangles. It takes four arguments: left, right, top, and bottom. These arguments specify the coordinates of the four corners of the rectangle. The quad() function returns a GlyphRenderer object


output_file("Graph1.html")
show(p)