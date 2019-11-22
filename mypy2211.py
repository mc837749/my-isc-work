###
#Chapter 1:
###

# EXERCISE 1

#Q1

#  open serial port

#!/usr/bin/env python
import serial
import io
from datetime import datetime

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE)

#Q2 

#  get data from temperature probe
print(ser.read(size=8)) #size 8 is specific to the Papouch thermometer device

#Q3

#  view the temperature with the corresponding date and time
datastring = ser.read(size=8)
print(datetime.utcnow().isoformat(), datastring)

#Q4

#  continuously log the data by add a while loop to read the time and temperature

while ser.isOpen():
    datastring = ser.read(size=8)
    print(datetime.utcnow().isoformat(), datastring)

#Q5

#  rewrite the code to use readline()
import io

sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser, 1), encoding='ascii', newline='\r')
sio._CHUNK_SIZE =1

while ser.isOpen():
    datastring = sio.readline()
    print(datetime.utcnow().isoformat(), datastring)

#Q6

#  alter the code to write the data out to a file

outfile='/tmp/serial-temperature.tsv'

ser = serial.Serial(
   port='/dev/ttyUSB0',
   baudrate=9600,
)

sio = io.TextIOWrapper(
   io.BufferedRWPair(ser, ser, 1), 
   encoding='ascii', newline='\r'
)
sio._CHUNK_SIZE =1

with open(outfile,'a') as f: #appends to existing file 
   while ser.isOpen():
      datastring = sio.readline()
      #\t is tab; \n is line separator
      f.write(datetime.utcnow().isoformat() + '\t' + datastring + '\n')
      f.flush() #included to force the system to write to disk

ser.close()


###
#Chapter 2: Writing and Plotting NetCDF files
###

#Q1

import serial
import io
from datetime import datetime

#  convert time to Python time

def convert_time(tm):
    tm = datetime.strptime(tm, '%Y-%m_%dT%H:%M:%S.%f')
    return tm

#Q2

#
def convert_temp(temp):
    value = temp.strip('+').strip)'C').lstrip('0')
    return float(value) + 273.15

#Q3

infile = 'sample-serial-teamperature-2h.tsv
outfile = 'sensor-data.nc'

from csv import reader

times = []
temps = []

with open(infile, 'rb') as tsvfile:
    tsvreader = reader(tsvfile, delimiter='\t')
    for row in tsvreader:
        times.append(convert_time(row[0]))
        temps.append(convert_time(row[1]))






