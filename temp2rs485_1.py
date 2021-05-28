import pymodbus
import serial
import time
from pymodbus.pdu import ModbusRequest
# initialize a serial RTU client instance
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.transaction import ModbusRtuFramer

import logging
# logging.basicConfig()
# log = logging.getLogger()
# log.setLevel(logging.DEBUG)

#count= the number of registers to read
#unit= the slave unit this request is targeting
#address= the starting address to read from

import sys


unit_input_list=[1,2,3,4,5,6]
temp_list = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
com_input = sys.argv[1]
unit_input = unit_input_list[0] # sys.argv[2]

print("연결포트::",com_input)
client = ModbusClient(method="rtu",  port=com_input,  stopbits=1, bytesize=8, parity='N', baudrate=9600)

#Connect to the serial modbus server
connection = client.connect()
print("connect-->",connection) 
pos = 0
while True:
    just_now = time.gmtime(time.time())
    
    tempstr='ts:'+str(just_now.tm_hour)+':'+str(just_now.tm_min)+'>>'
    for pos in range(6):

        temps = client.read_input_registers(1000, 2, unit=unit_input_list[pos])  # address, count, slave address
        print(unit_input_list[pos])
        val= temps.registers[1]
       
        point = 1;
        if(val == 1):
            point = 10
        elif(val==2):
            point = 100
        elif(val == 3):
            point = 1000

        temp_list[pos]=temps.registers[0]/point
        #print(temp_list[pos])
    print(">>",tempstr,"온도", temp_list)
    time.sleep(60)
        #coil = client.read_coils(0, 3, unit=1)  # address, count, slave address
        #print ("온도:",coil)


#Closes the underlying socket connection
client.close()
