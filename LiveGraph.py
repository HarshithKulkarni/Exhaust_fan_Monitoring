import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

def animate(i, xs, ys):

    data = pd.read_csv("Dataset.csv")
    
    for i in range(len(data['Mon']+1)):

        velocity = (data.iloc[i][7])       
        """month = int(data.iloc[i][0])
        date = int(data.iloc[i][1])
        year = int(data.iloc[i][2])
        hour = int(data.iloc[i][3])
        minute = int(data.iloc[i][4])
        sec = int(data.iloc[i][5])
        microsec = int(data.iloc[i][6])
        xs.append(datetime.datetime(year,month,date,hour,minute,sec,microsec).strftime('%H:%M:%S.%f'))"""
        xs.append(datetime.datetime.now().strftime('%H:%M:%S.%f'))
        ys.append(velocity)

    # Limit x and y lists to 20 items
    xs = xs[-5:]
    ys = ys[-5:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Velocity vs Time')
    plt.ylabel('Velocity')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys),interval=100)
plt.show()
