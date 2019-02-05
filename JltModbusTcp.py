from pyModbusTCP.client import ModbusClient


class JltModbusTcp(ModbusClient):
    def __init__(self, host = 'localhost', port = 502):
        super(JltModbusTcp, self).__init__(host=host, port=port)
        self.inputRegs = None
        self.holdingRegs = None
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

    def readInput(self, regName, size=2):
        data = self.read_input_registers(self.inputRegs[regName]['regNr'], size)
        if not data:
            raise Exception('readInputExtraLong: read error')
        return self.dataToInt(data)

    def readHolding(self, regName, size=2):
        data = self.read_holding_registers(self.holdingRegs[regName]['regNr'], size)
        if not data:
            raise Exception('readHoldingExtraLong: read error')
        return self.dataToInt(data)

    def write(self, regName, value, size=2):
        data = [((value >> (i*16)) & 0xFFFF) for i in range(size)]
        ret = self.mbTcp.write_multiple_registers(self.holdingRegs[regName]['regNr'], data)
        if not ret:
            raise Exception('writeHoldingExtraLong: write error')

    # *********************************************************************
    # HIGHER LEVEL FUNCTIONS DEFINITIONS
    # *********************************************************************
    def readFormatedInput(self, reg):
        try:
            size = self.inputRegs[reg]['size']
        except ValueError:
            size = 1
        val = self.readInput(reg, size)
        if self.inputRegs[reg]['format'] == 'F':
            return round(val * 0.1, 1)
        elif self.inputRegs[reg]['format'] == 'IS':
            return val if not val & 0x8000 else val & 0x7FFF - 0xFFFF
        return val

    def readFormatedHolding(self, reg):
        try:
            size = self.holdingRegs[reg]['size']
        except ValueError:
            size = 1
        val = self.readHolding(reg, size)
        if self.holdingRegs[reg]['format'] == 'F':
            return round(val * 0.1, 1)
        elif self.holdingRegs[reg]['format'] == 'IS':
            return val if not val & 0x8000 else val & 0x7FFF - 0xFFFF
        return val


    def writeFormatedHolding(self, reg, value):
        try:
            size = self.holdingRegs[reg]['size']
        except ValueError:
            size = 1
        if self.holdingRegs[reg]['format'] == 'F':
            value = int(value * 10)
        elif self.holdingRegs[reg]['format'] == 'IS':
            value = value & 0xFFFF if value >= 0 else value & 0xFFFF | 0x8000
        data = [((value >> (i * 16)) & 0xFFFF) for i in range(size)]
        ret = self.write_multiple_registers(self.holdingRegs[reg]['regNr'], data)
        if not ret:
            raise Exception('writeFormatedHolding: write error')

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
        return self.readInput('fut_temp_ambient', 1) * 0.1

    def temp_fresh(self):
        return self.readInput('fut_temp_fresh', 1) * 0.1

    def temp_indoor(self):
        return self.readInput('fut_temp_indoor', 1) * 0.1

    def temp_waste(self):
        return self.readInput('fut_temp_waste', 1) * 0.1

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
        return self.readHolding('cfg_temp_set', 1) * 0.1