import statistics
import csv
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff
import random 

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

fig = ff.create_distplot([data], ["reading time"], show_hist = False)
fig.show()

print("The mean is", statistics.mean(data))

def random_set_of_numbers(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    figure = ff.create_distplot([mean_list], ["temp"], show_hist = False)
    figure.show()

def setup():
    mean_list = []
    for i in range(0, 100):
        set_of_means = random_set_of_numbers(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

