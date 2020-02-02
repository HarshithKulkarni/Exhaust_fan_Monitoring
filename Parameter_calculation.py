import pandas as pd
import datetime
import numpy as np
import math
import time

class calculation:

    def __init__(self):

        self.dateparser = lambda date_time: pd.datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S.%f")
        self.data= pd.read_csv("data_nov28_7PM.txt", names=['date_time', 'Velocity'],sep = ",",header = None,index_col = False,parse_dates=['date_time'],date_parser=self.dateparser)
        #time = self.data.date_time[0].strftime('%S')
        #print(time)
    def acceleration(self):
        
        self.accel = []
        for i in range(len(self.data)):
            
            try:
                date2 = self.data.date_time[i+1]
                date1 = self.data.date_time[i]
                velo2 = self.data.Velocity[i+1]
                velo1 = self.data.Velocity[i]
                acc = (velo2-velo1)/(date2-date1).total_seconds()
                self.accel.append(acc)
                
            except:
                pass
        #return self.accel
    
    def velocity_rms(self):
        self.rms_arr = []
        rms_val = 0
        #print("Velocity RMS:")
        for i in range(len(self.data)):
            count = i
            if(int(self.data.date_time[i].strftime('%S'))%5!=0):
                rms_val = rms_val+(self.data.Velocity[i])**2
            elif(int(self.data.date_time[i].strftime('%S'))%5==0):
                rms_val = rms_val+(self.data.Velocity[i])**2
                time.sleep(5)
                i = count
            rms = math.sqrt(rms_val/5)
            self.rms_arr.append(rms)
            #print(rms)
            #return self.rms_arr
    
    def velocity_peak(self):
        velo_peak_arr = []
        #print("Velocity Peak:")
        for u in (self.rms_arr):
            velo_peak = 2*math.sqrt(2)*u
            velo_peak_arr.append(velo_peak)
            #print(velo_peak)
        #return velo_peak_arr

    def acceleration_rms(self):

        self.acc_rms_arr = []
        acc_rms_val = 0
        #print("Acceleration RMS:")
        for i in range(len(self.accel)):
            count = i
            if(int(self.data.date_time[i].strftime('%S'))%5!=0):
                acc_rms_val = acc_rms_val+(self.accel[i])**2
            elif(int(self.data.date_time[i].strftime('%S'))%5==0):
                acc_rms_val = acc_rms_val+(self.accel[i])**2
                time.sleep(5)
                i = count
            acc_rms = math.sqrt(acc_rms_val/5)
            self.acc_rms_arr.append(acc_rms)
            print(acc_rms)
        #return self.acc_rms_arr
    
    def acceleration_peak(self):
        
        acc_peak_arr = []
        #print("Acceleration Peak:")
        for u in (self.acc_rms_arr):
            acc_peak = 2*math.sqrt(2)*u
            acc_peak_arr.append(acc_peak)
            #print(acc_peak)
        #return acc_peak_arr

obj = calculation()
obj.acceleration()
obj.velocity_rms()
obj.velocity_peak()
obj.acceleration_rms()