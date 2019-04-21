import matplotlib.pyplot as plt
import csv
import pandas as pd



data0=pd.read_csv('access.log',header=None, delimiter='\t')
latency=pd.Series(data0[11])
date=pd.Series(data0[0])

cleanedlatency = [x for x in latency if str(x) != 'nan']
cleaneddate = [x for x in date if str(x) != 'nan']

df = pd.DataFrame({
'latencies': cleanedlatency,
'dates': cleaneddate
})
hist = df.hist(bins=3)



# with open('access.log','r') as csvfile:
#     plots = csv.reader(csvfile, delimiter='\t')
#     for row in plots:
#         x.append(int(row[0]))
#         y.append(int(row[1]))

plt.plot(cleanedlatency,cleaneddate)
plt.xlabel('latency')
plt.ylabel('date')
plt.title('Latency distribution\n Useful for logfile analysis')
plt.legend()
plt.show()