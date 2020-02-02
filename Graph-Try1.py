from matplotlib import pyplot as plt
from matplotlib import animation 
import pandas as pd
import datetime

class Graph:
    
    def __init__(self):

        self.data = pd.read_csv("Dataset.csv")

    def append_to_list(self):

        self.time_array = []
        self.velocity_array = []
        self.acceleration_array = []

        for i in range(len(self.data['Mon']+1)):

            sec = int(self.data.iloc[i][5])
            velocity = (self.data.iloc[i][7])
            acceleration = self.data.iloc[i][8]    
            self.time_array.append(i)
            self.velocity_array.append(velocity)
            self.acceleration_array.append(acceleration)

    def velocity_vs_time(self):

        plt.plot(self.time_array, self.velocity_array) 
        plt.xlabel('Time(Sec)--->') 
        plt.ylabel('Velocity') 
        plt.title('Velocity vs Time') 
        plt.show()

    def acceleration_vs_time(self):

        plt.plot(self.time_array, self.acceleration_array) 
        plt.xlabel('Time(Sec)--->') 
        plt.ylabel('Acceleration') 
        plt.title('Acceleration vs Time') 
        plt.show()

o = Graph()
o.append_to_list()
#o.velocity_vs_time()
#o.acceleration_vs_time()
