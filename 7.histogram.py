import matplotlib.pyplot as plt
import numpy as np

arr = np.array([10,45,20,36,95,78,25,45,36,21,45,68,23,65,45,69])

plt.hist(arr,bins=[0,20,40,60,80]) # the bins parameter sets the nins i.e integer or sequence

plt.xlabel("Students")
plt.ylabel("Marks")

plt.title("Title")

plt.show()