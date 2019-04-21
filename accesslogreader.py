import matplotlib.pyplot as plt
import csv
import pandas as pd



data0=pd.read_csv('access.log',header=None, delimiter='\t')
latency=pd.Series(data0[11])
date=pd.Series(data0[0])




# with open('access.log','r') as csvfile:
#     plots = csv.reader(csvfile, delimiter='\t')
#     for row in plots:
#         x.append(int(row[0]))
#         y.append(int(row[1]))

plt.plot(latency,date)
plt.xlabel('latency')
plt.ylabel('date')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()