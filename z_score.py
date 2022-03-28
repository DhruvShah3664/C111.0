import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics 
import random
import plotly.graph_objects as go

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list=[]
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

mean = statistics.mean(data)
std = statistics.stdev(data)
print("Mean of sample: ",mean)
print("Standard deviation of sample: ",std)

#finding  the standard deviation starting and ending values
first_std_start,first_std_end = mean - std, mean + std
second_std_start, second_std_end = mean - (2* std), mean + (2* std)
third_std_start, third_std_end = mean - (3* std), mean + (3* std)

#print(" STD 1: ", first_std_start, first_std_end)
#print(" STD 2: ", second_std_start, second_std_end)
#print(" STD 3: ", third_std_start, third_std_end)

#finding the mean of the STUDENTS WHO GAVE EXTRA TIME TO MATH LAB and plot the graph
df = pd.read_csv("school_1_sample.csv")
data = df["Math_score"].tolist()

mean_of_sample1 = statistics.mean(data)
print("The mean of sample 1: ", mean_of_sample1)

fig = ff.create_distplot([mean_list], ["Math Score"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1,mean_of_sample1],y=[0,0.17],mode="lines",name="MEAN OF SAMPLE 1"))
fig.add_trace(go.Scatter(x=[first_std_end,first_std_end],y=[0,0.17],mode="lines",name="STANDARD_DEVIATION_1_end"))
fig.add_trace(go.Scatter(x=[second_std_end,second_std_end],y=[0,0.17],mode="lines",name="STANDARD_DEVIATION_2_end"))
fig.add_trace(go.Scatter(x=[third_std_end,third_std_end],y=[0,0.17],mode="lines",name="STANDARD_DEVIATION_3_end"))
fig.show()

#finding the mean of the STUDENTS WHO USED MATH PRACTICE APP and plot the graph

df = pd.read_csv("school_2_sample.csv")
data = df["Math_score"].tolist()

mean_of_sample2 = statistics.mean(data)
print("The mean of sample 2: ", mean_of_sample2)

fig = ff.create_distplot([mean_list], ["Math Score"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample2,mean_of_sample2],y=[0,0.17],mode="lines",name="MEAN OF SAMPLE 2"))
fig.add_trace(go.Scatter(x=[first_std_end,first_std_end],y=[0,0.17],mode="lines",name="STANDARD_DEVIATION_1_end"))
fig.add_trace(go.Scatter(x=[second_std_end,second_std_end],y=[0,0.17],mode="lines",name="STANDARD_DEVIATION_2_end"))
fig.add_trace(go.Scatter(x=[third_std_end,third_std_end],y=[0,0.17],mode="lines",name="STANDARD_DEVIATION_3_end"))
fig.show()

#finding the mean of the STUDENTS WHO WERE ENFORCED WITH REGISTERS and plot the graph

df = pd.read_csv("school_3_sample.csv")
data = df["Math_score"].tolist()

mean_of_sample3 = statistics.mean(data)
print("The mean of sample 3: ", mean_of_sample3)

fig = ff.create_distplot([mean_list], ["Math Score"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample3,mean_of_sample3],y=[0,0.17],mode="lines",name="MEAN OF SAMPLE 3"))
fig.add_trace(go.Scatter(x=[first_std_end,first_std_end],y=[0,0.17],mode="lines",name="STANDARD_DEVIATION_1_end"))
fig.add_trace(go.Scatter(x=[second_std_end,second_std_end],y=[0,0.17],mode="lines",name="STANDARD_DEVIATION_2_end"))
fig.add_trace(go.Scatter(x=[third_std_end,third_std_end],y=[0,0.17],mode="lines",name="STANDARD_DEVIATION_3_end"))
fig.show()

#finding the z score using the formula 
z_score = (mean - mean_of_sample1)/std
print("The z score is: ", z_score)

