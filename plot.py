import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pings = pd.read_csv("p.csv", sep="\t", header=None, names=["time"])

print("Min:", np.min(pings.time))
print("Mean:", np.mean(pings.time))
print("Std Dev:", np.std(pings.time))
print("Max:", np.max(pings.time))


plt.figure(figsize=(14,8))
plt.xlabel("idx")
plt.ylabel("time (ms)")
plt.plot(pings.time)
plt.savefig("pings.png")
