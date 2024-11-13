import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ODetails = pd.read_csv('Order_details(masked).csv')
ODetails.info();

# here we have taken Transaction Date column of the csv file
ODetails['Time'] = pd.to_datetime(ODetails['Transaction Date'])

#Extracting hour from transaction
ODetails['Hour'] = (ODetails['Time']).dt.hour

#This is to determine the busiest hour in terms of purchases
tmost1 = ODetails['Hour'].value_counts().index.tolist()[:24]

tmost2 = ODetails['Hour'].value_counts().values.tolist()[:24]

tmost = np.column_stack((timemost1,timemost2))

print(" Hour Of Day" + "\t" + "Cumulative Number of Purchases \n")
print('\n'.join('\t\t'.join(map(str, row)) for row in tmost))

timemost = ODetails['Hour'].value_counts()
timemost1 = []

for i in range(0,23):
	timemost1.append(i)

timemost2 = timemost.sort_index()
timemost2.tolist()
timemost2 = pd.DataFrame(timemost2)

#plotting of the graph
plt.figure(figsize=(10, 10))

plt.title('Sales Happening Per Hour (Spread Throughout The Week)',
		fontdict={'fontname': 'monospace', 'fontsize': 30}, y=1.05)

plt.ylabel("Number Of Purchases Made", fontsize=18, labelpad=20)
plt.xlabel("Hour", fontsize=18, labelpad=20)
plt.plot(timemost1, timemost2, color='m')
plt.grid()
plt.show()