import csv
import plotly.figure_factory as ff
import pandas as pd
import statistics
import plotly.graph_objects as go

with open("Projects\StudentsPerformance.csv", newline='') as f:
    fr =csv.reader(f)
    df=list(fr)

df.pop(0)

new_data=[]

for i in range(len(df)):
    value = df[i][7]
    new_data.append(float(value))

mean = statistics.mean(new_data)

stdv = statistics.stdev(new_data)

print("STDV: ",stdv," MEAN: ",mean)

median = statistics.median(new_data)

mode = statistics.mode(new_data)
print("MEDIAN: ",median," MODE: ",mode)

first_stdev_start,first_stdev_end = mean- stdv, mean+stdv

list_first=[]
for i in range(0, len(new_data)):
    if(new_data[i]>=first_stdev_start and new_data[i]<= first_stdev_end):
        list_first.append(new_data[i])

percentage_first= (len(list_first)*100)/len(new_data)
print(percentage_first)


second_stdev_start,second_stdev_end = mean- (2*stdv), mean+(2*stdv)

list_second=[]
for i in range(0, len(new_data)):
    if(new_data[i]>=second_stdev_start and new_data[i]<= second_stdev_end):
        list_second.append(new_data[i])

percentage_second= (len(list_second)*100)/len(new_data)
print(percentage_second)

third_stdev_start,third_stdev_end = mean- (3*stdv), mean+(3*stdv)

list_third=[]
for i in range(0, len(new_data)):
    if(new_data[i]>=third_stdev_start and new_data[i]<= third_stdev_end):
        list_third.append(new_data[i])

percentage_third= (len(list_third)*100)/len(new_data)
print(percentage_third)



fig = ff.create_distplot([new_data],["Reading Score"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.1],mode="lines",name="MEAN"))

fig.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start],y=[0,0.1],mode="lines",name="STD_1_START"))

fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.1],mode="lines",name="STD_1_END"))

fig.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,0.1],mode="lines",name="STD_2_START"))

fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.1],mode="lines",name="STD_2_END"))

fig.show()