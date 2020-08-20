'''
    graph.py -- Description: Plots a graph diplaying inflation
                                 rate every 30 years for 500 years.
                                 Data is generated into and read from
                                 a text file.
                    Note: This version has more information yet more cluttered
                    Args: 'example.txt'
    Author: Amr Abdallah
    ID    : C0744378
'''
# Libraries Imported
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.patches
import random
import numpy as np
import matplotlib.dates as mdates
import sys

style.use('fivethirtyeight')        # style used for graph ploted        

fig = plt.figure()                  # graph parameters set
ax1 = fig.add_subplot(1,1,1)        # utility wrapper makes it convenient _ 
                                    # to create common layouts of subplots
fileName = 'example.txt'
xIncrement = 1600                   # Begins x-axis increments

# flag that is fired once to create file
# in case it's not there and empty's the
# file if it exists and ready it for first use.
Started = False

# Clear File Content
def clearFile():
    file= open(fileName,"w+")
    file.close()

# Function respnsible for graph animation
def animate(i):
    #print(sys.argv)
    global fileName     # file name can be obtained from command-line or _
                        # works on set default value in case it works from here
    if len(sys.argv) == 2:                      # checks number of CLA
        if str(sys.argv[1])[-4:] == '.txt':     # makes sure filename is a text file
            fileName = str(sys.argv[1])         # gets filename from CLA
            #print(str(sys.argv[1])[-4:])
    
    global Started                              # global flag declared

    # flag that is fired once to create file
    # in case it's not there and empty's the
    # file if it exists and ready it for first use.
    if Started == False or xIncrement > 2000:                        
        clearFile()
        Started = True
        
    # calls fileWrite function    
    fileWrite()                                 # writes generated data to file
    
    with open(fileName, "r") as f:              # read generated values from file
        graph_data = f.read()
    lines = graph_data.split('\n')              # parse file lines
    xs = []                                     # 30 generated Values x-axis 
    ys = []                                     # 30 generated Values y-axis

    # populating x-axis and y-axis lists from file
    for line in lines:
        if len(line) > 1:
            x,y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))

    # Preparing max ticker values - it's important to cast them to float
    # otherwise they are not properly sorted when graph is ploted
    xMax = float(max(xs))
    #print(xMax)
    yMax = float(max(ys))
    #print(yMax)
    ax1.clear()

    # Graph axis lables, title and ticks
    plt.xlabel("Years")
    plt.ylabel("inflation")
    plt.yticks(np.arange(0, yMax + 4, 0.25))
    plt.xticks(np.arange(0, xIncrement+30, 5))
    plt.ylim(0, 6) # limit on Y axis (modify to fit your data
    ax1.plot(xs, ys)
    ax1.set_title('Inflation over 500 years')

    # getting points for maximum inflation rate
    ymax = max(ys)
    xpos = ys.index(ymax)
    xmax = xs[xpos]

    # Annotation Arrow moves based on newly plotted values
    ax1.annotate('Highest Inflation {:.2f}'.format(ymax), xy=(xmax, ymax), xytext=(xmax, ymax+5),
                 arrowprops=dict(facecolor='red', shrink=0.05),)
    ##        arrowprops=dict(facecolor='red',arrowstyle="fancy",
    ##                        connectionstyle="arc3,rad=-4.2"),
    ##             horizontalalignment='right', verticalalignment='bottom',)
 
    ##ax1.annotate('local max', xy=(xmax, ymax), xytext=(xmax, ymax+5), arrowprops=dict(facecolor='black', shrink=0.05),)

    # getting x-axis values to tilt when autofomated as date to conserve space
    # Plotting a big clear graph canvas
    g = plt.gcf()
    plt.gcf().autofmt_xdate()
    g.set_size_inches(14,7)

# calls animate function to refresh graph with new data every 3 seconds
ani = animation.FuncAnimation(fig, animate, interval = 3000)

# writes Generated values to file
def fileWrite():
    #clearFile()
    file= open(fileName,"a+")       # keeps appending file as long as program is running
    for i in range(30):             # Adds 30 values per intrival to file
        global xIncrement           # makes increment avaliable globally
        xIncrement = xIncrement + 1 # adding increments
        # formating line to be written in file
        line = '{:.2f},{:.2f}\n'.format(xIncrement,random.uniform(0.1,5)) # generating inflation y-axis float random values
        file.write(line) # writing values to file 

    #print(line)
    file.close()    #close file
    

plt.show()      # Show graph with setting and values
