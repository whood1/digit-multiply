import numpy as np 
import matplotlib as mp 
import matplotlib.pyplot as plt
import pandas as pd 

def buildLinePlot(xdata, ydata):
	out = plt.plot(xdata, ydata, 'rx' )
	plt.axis([0, 1.2e14, 0, 15])
	return out

df = pd.read_csv('data.csv')

ndArr = df.to_numpy()

print('[ndArray]\n')
print(ndArr)

ndArr_split = np.hsplit(ndArr, 3)
print('split up [ndArray]\n')
print(ndArr_split)

xdata = ndArr_split[1]
ydata = ndArr_split[2]

#xdata = [1, 2, 3, 4, 5, 6, 7, 8, 100]
#ydata = [1, 1, 1, 1, 1, 1, 1, 1, 1]
print('XDATA \n')
print(xdata)
print('YDATA \n')
print(ydata)

fig, ax = plt.subplots()
plot1 = buildLinePlot(xdata, ydata)


plt.show()



