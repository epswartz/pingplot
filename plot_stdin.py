import time
from threading import Thread, Event
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import fileinput
import re
import sys
import numpy as np
import os

TIME_REGEX = 'time=\d+\.?\d*'


# TODO should be ndarray from the jump.
pingTimes = []

event = Event()

# Continuously read from stdin and update pings
def readTimes():
    l = 0 # this is for faking numbers TODO get real ones
    while True:
        try:
            if not event.is_set():
                line = sys.stdin.readline()
                if "time" in line:
                   newTime = line[line.rindex("=")+1:line.rindex(" ")]
                   print("Time:", newTime, "ms")
                   pingTimes.append(float(newTime))
            time.sleep(0.5)
        except KeyboardInterrupt:
            return


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    event.set()
    xs = np.arange(len(pingTimes))
    ys = np.asarray(pingTimes)
    event.clear()
    ax1.clear()
    ax1.plot(xs,ys)
    ax1.set_xlabel("icmp_seq")
    ax1.set_ylabel("time (ms)")
    ax1.set_ylim(0,np.max(ys)*1.1)

readerThread = Thread(target=readTimes)
readerThread.start()
time.sleep(4)
ani = animation.FuncAnimation(fig, animate, interval=1000)

plt.show()
readerThread.join()
