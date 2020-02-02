import pandas as pd
import datetime as dt
class calculate:

    def __init__(self):

        self.df = pd.read_csv("DataSet.csv")
        x = self.df.iloc[0][0]
        month = x[slice(0,2)]
        date = x[slice(3,5)]
        year = x[slice(6,10)]
        hour = x[slice(12,14)]
        minute = x[slice(15,17)]
        sec = x[slice(18,20)]
        micsec = x[slice(21,27)]
        print(month,date,year,hour,minute,sec,micsec)               
    def write(self):
        
        for i in range(len(self.df['Column1'])+1):
            try:
                x = self.df.iloc[i][0]
                velo = str(self.df.iloc[i][1])
                month = x[slice(0,2)]
                date = x[slice(3,5)]
                year = x[slice(6,10)]
                hour = x[slice(12,14)]
                minute = x[slice(15,17)]
                sec = x[slice(18,20)]
                micsec = x[slice(21,27)]
                f = open("Database.txt","a")
                f.write(month)
                f.write("\t")
                f.write(date)
                f.write("\t")
                f.write(year)
                f.write("\t")
                f.write(hour)
                f.write("\t")
                f.write(minute)
                f.write("\t")
                f.write(sec)
                f.write("\t")
                f.write(micsec)
                f.write("\t\t")
                f.write(velo)
                f.write("\n")
                f.close()
            except IndexError:
                pass
o = calculate()
o.write()