import matplotlib.pyplot as plt
import csv
import numpy as np
import time
import datetime

rh = []
t = []
p = []
acc_x = []
acc_y = []
acc_z = []
vcc = []
vpd = []
vbat = []
date = []

with open('data/stream_data_27.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    csvfile.next() # skip first row
    for row in plots:
		vcc.append(int(row[0]))
		vpd.append(int(row[2]))
		acc_z.append(int(row[5]))
		p.append(float(row[6]))
		vbat.append(int(row[7]))
		t.append(float(row[8]))
		rh.append(float(row[10]))
		acc_y.append(int(row[12]))
		acc_x.append(int(row[13]))
		date.append(str(row[14]))
Time = [time.mktime(datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ").timetuple()) for date in date]
StartTime = Time[-1]
TimePlot = np.subtract(Time, StartTime)
TimePlot = TimePlot/(24*60*60)


plt.figure(0)
plt.plot(TimePlot,vcc, label='vcc')
plt.plot(TimePlot,vbat, label='vbat')
plt.plot(TimePlot,vpd, label='vpd')
plt.xlabel('Time (days)')
plt.ylabel('Voltage (V)')
plt.title('Power Plot')
plt.legend()
plt.savefig('images/plot0.png', format='png')

plt.figure(1)
plt.title('Environmental parameters')
plt.subplot(211)
plt.plot(TimePlot,t, label='t')
plt.plot(TimePlot,rh, label='rh')
plt.subplot(212)
plt.plot(TimePlot,p, label='p')
plt.xlabel('Time (days)')
plt.ylabel('Pressure (mbar)')
plt.legend()
plt.savefig('images/plot1.png', format='png')

plt.figure(2)
plt.plot(TimePlot,acc_x, label='X')
plt.plot(TimePlot,acc_y, label='Y')
plt.plot(TimePlot,acc_z, label='Z')
plt.xlabel('Time (days)')
plt.ylabel('Acceleration')
plt.title('Accelerometer')
plt.legend()
plt.savefig('images/plot2.png', format='png')

plt.show()
