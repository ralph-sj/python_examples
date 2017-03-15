############################################################
############################################################
# PLOT_SENSOR_DATA/PLOT_DATA.py
# Read in data from file within DATA folder in format
# col:		0	2	5	6	7	8	10	12	13	14
# variable: 	VCC	VPD	ACC_Z	P	VBAT	T	RH	ACC_Y	ACC_X	DATE
# Variable are then plotted against date (formatted in days) on 3 graphs
# Plots are saved in IMAGES folder
############################################################
############################################################

## IMPORT MODULES
import matplotlib.pyplot as plt
import csv
import numpy as np
import time
import datetime

## INITIALISE VARIABLES TO HOLD DATA
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

## READ IN DATA FROM FILE
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
		date.append(str(row[14])) # date string (in "%Y-%m-%dT%H:%M:%S.%fZ" format)

## PROCESS TIME/DAT VARIABLE
Time = [time.mktime(datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ").timetuple()) for date in date] # convert string to serial time (in seconds)
StartTime = Time[-1] # find start time (last element in Time array)
TimePlot = np.subtract(Time, StartTime) # calculate relative to start time
TimePlot = TimePlot/(24*60*60) # convert to days from seconds

## VCC, VBAT & VPD
plt.figure(0)
plt.plot(TimePlot,vcc, label='vcc')
plt.plot(TimePlot,vbat, label='vbat')
plt.plot(TimePlot,vpd, label='vpd')
plt.xlabel('Time (days)')
plt.ylabel('Voltage (V)')
plt.title('Power Plot')
plt.legend()
plt.savefig('images/plot0.png', format='png')

## T, RH & P (subplot)
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

## ACCELEROMTER
plt.figure(2)
plt.plot(TimePlot,acc_x, label='X')
plt.plot(TimePlot,acc_y, label='Y')
plt.plot(TimePlot,acc_z, label='Z')
plt.xlabel('Time (days)')
plt.ylabel('Acceleration')
plt.title('Accelerometer')
plt.legend()
plt.savefig('images/plot2.png', format='png')


## DISPLAY PLOTS
plt.show()
