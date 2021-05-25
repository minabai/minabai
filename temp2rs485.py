#Import useful modules
import time
from pymodbus.client.sync import ModbusSerialClient as ModbusClient

#For the first test, I manually read the configuration from the
#the controller display and hard-code the values in the script.
d_port = 'COM3'  # Device address
commspeed = {}  # Communication speed
commspeed_table = {
    '0': 2400,
    '1': 4800,
    '2': 9600,
    '3': 19200,
}
commspeed['flag'] = '2'
commspeed['value'] = commspeed_table[commspeed['flag']]
bitconf = {}  # Bit configuration
bitconf_table = {
    '0': (8, 'N', 1),
    '1': (8, 'N', 2),
    '2': (7, 'E', 1),
    '3': (7, 'E', 2),
    '4': (7, 'O', 1),
    '5': (7, 'O', 2),
}
bitconf['flag'] = '0'
bitconf['size'], bitconf['parity'], bitconf['stopbit'] =\
    bitconf_table[bitconf['flag']]
intime = {}
intime['flag'] = '5'
intime['value'] = round(int(intime['flag'])*1.666, 0)


def main():
    modbus = ModbusClient(method='ascii', port='COM3',
                          baudrate=commspeed['value'], stopbits=bitconf['stopbit'],
                          bytesize=bitconf['size'], parity=bitconf['parity'],
                          timeout=1)
    modbus.connect()
    while(1):
        r = modbus.read_holding_registers(0x0000, 1)
        print(r)
        time.sleep(1)




if __name__ == "__main__":
    main()
