from pyModbusTCP.client import ModbusClient
from futuraMbRegisters import *




class JltModbusTcp(ModbusClient):
    def __init__(self, host='localhost', port=502):
        super(JltModbusTcp, self).__init__(host=host, port=port, auto_open=True, auto_close=True)
        self.inputRegs = futuraInputRegisters
        self.holdingRegs = futuraHoldingRegisters
    # *********************************************************************
    # LOW LEVEL FUNCTIONS DEFINITIONS
    # *********************************************************************
    def dataToInt(self, data):
        shift = 0
        result = 0
        for i in data:
            result |= i << shift
            shift += 16
        return result

    def readInput(self, regName, size=1):
        data = self.read_input_registers(self.inputRegs[regName]['regNr'], size)
        if not data:
            raise Exception('readInputExtraLong: read error')
        return self.dataToInt(data)

    def readHolding(self, regName, size=1):
        data = self.read_holding_registers(self.holdingRegs[regName]['regNr'], size)
        if not data:
            raise Exception('readHoldingExtraLong: read error')
        return self.dataToInt(data)

    def writeHolding(self, regName, value, size=1):
        data = [((value >> (i*16)) & 0xFFFF) for i in range(size)]
        ret = self.write_multiple_registers(self.holdingRegs[regName]['regNr'], data)
        if not ret:
            raise Exception('writeHoldingExtraLong: write error')


    # *********************************************************************
    # READ FORMATED MODBUS HOLDING REGISTERS
    # *********************************************************************
    def readFormatedHolding(self, regName):
        try:
            size = int(self.holdingRegs[regName]['size'])
        except ValueError:
            size = 1

        power = 1
        val = self.readHolding(regName, size)
        if self.isNumber( self.holdingRegs[regName]['power']):
           power = self.holdingRegs[regName]['power'] * 1.0

        if self.holdingRegs[regName]['format'] == 'F':
            return round(val * 0.1, 1)
        elif self.holdingRegs[regName]['format'] in ['IS', 'SINT']:
            if val & 0x8000:
                val = val & 0x7FFF - 0xFFFF
                val = val * -1.0

        if power != 1:
            return round(val/power, 1)
        else:
            return int(val)


    # *********************************************************************
    # READ FORMATED MODBUS INPUT REGISTERS
    # *********************************************************************
    def readFormatedInput(self, regName):
        try:
            size = int(self.inputRegs[regName]['size'])
        except ValueError:
            size = 1

        power = 1
        val = self.readInput(regName, size)
        if self.isNumber( self.inputRegs[regName]['power']):
           power = self.inputRegs[regName]['power'] * 1.0

        if self.inputRegs[regName]['format'] == 'F':
            return round(val * 0.1, 1)
        elif self.inputRegs[regName]['format'] in ['IS', 'SINT']:
            if val & 0x8000:
                val = val & 0x7FFF - 0xFFFF
                val = val * -1.0

        if power > 1:
            return round(val/power, 1) if val>0 else 0
        else:
            return int(val)


    # *********************************************************************
    # READ FORMATED MODBUS HOLDING REGISTERS
    # *********************************************************************
    def writeFormatedHolding(self, regName, value):
        try:
            size = int(self.holdingRegs[regName]['size'])
        except ValueError:
            size = 1

        power = 1
        if self.isNumber( self.holdingRegs[regName]['power']):
           power = self.holdingRegs[regName]['power'] * 1.0

        value = float(value) if self.isNumber(value) else eval(value)
        value *= power
        value = round(value)

        if self.holdingRegs[regName]['format'] in ['IS', 'SINT']:
            if value < 0:
                value = (0xFFFF - abs(value)) | 0x8000
            else:
                value = value & 0x7FFF
        print(value, size)
        self.write(regName, value, size)


    # *********************************************************************
    # HIGHT LEVEL FUNC
    # *********************************************************************
    def mac_address(self):
        #print('{:012X}'.format(mac))
        return self.readInput('mac_address0', 3)

    def serial_number(self):
        return self.readInput('serial_number0', 2)

    def hw_version(self):
        return self.readInput('hw_version0', 2)

    def fw_version(self):
        return self.readInput('fw_version0', 2)

    def sys_build_number(self):
        return self.readInput('sys_build_number0', 2)

    def sys_regmap_version(self):
        return self.readInput('sys_regmap_version0', 2)

    def sys_error(self):
        return self.readInput('sys_error0', 2)

    def sys_warning(self):
        return self.readInput('sys_warning0', 2)

    def temp_ambient(self):
        return round(self.readInput('fut_temp_ambient', 1) * 0.1, 1)

    def temp_fresh(self):
        return round(self.readInput('fut_temp_fresh', 1) * 0.1, 1)

    def temp_indoor(self):
        return round(self.readInput('fut_temp_indoor', 1) * 0.1, 1)

    def temp_waste(self):
        return round(self.readInput('fut_temp_waste', 1) * 0.1, 1)

    def humi_ambient(self):
        return self.readInput('fut_humi_ambient', 1) * 0.1

    def humi_fresh(self):
        return self.readInput('fut_humi_fresh', 1) * 0.1

    def humi_indoor(self):
        return self.readInput('fut_humi_indoor', 1) * 0.1

    def humi_waste(self):
        return self.readInput('fut_fut_humi_waste', 1) * 0.1

    def fan_supply_rpm(self):
        return self.readInput('fut_fan_rpm_supply', 1)

    def fan_exhaust_rpm(self):
        return self.readInput('fut_fan_rpm_exhaust', 1)

    def heating_power(self):
        return self.readInput('fut_heating_power', 1)

    def temp_set(self):
        print(self.readHolding('cfg_temp_set', 1))
        return round(self.readHolding('cfg_temp_set', 1) * 0.1, 1)