from pyModbusTCP.client import ModbusClient
from futuraMbRegisters import *
import time
import struct

class FuturaLibrary(object):
    def __init__(self):
        self._mbClient = None
    
    def open_client(self, hostAddr = 'localhost'):
        if self._mbClient:
            raise AssertionError('Modbus client is already opened!')
        self._mbClient = ModbusClient(host=hostAddr, port=502, auto_open=True)
        if not self._mbClient:
            raise AssertionError('Modbus client cannot be opened.')

    def read_holding_register(self, reg):
        data = self._mbClient.read_holding_registers(futuraHoldingRegisters[reg], 1)
        if not data:
            raise AssertionError('Holding named register %s cannot be read.' % reg)
        return data[0]

    def read_holding_register_long(self, reg):
        data = self._mbClient.read_holding_registers(futuraHoldingRegisters[reg], 2)
        if not data:
            raise AssertionError('Holding long register %s cannot be read.' % reg)
        return data[0] | ( data[1] << 16 )

    def write_register(self, reg, value):
        if not self._mbClient.write_single_register(futuraHoldingRegisters[reg], int(value)):
            raise AssertionError('Holding named register %s cannot be written.' % reg)

    def read_input_register(self, reg):
        data = self._mbClient.read_input_registers(futuraInputRegisters[reg], 1)
        if not data:
            raise AssertionError('Input named register %s cannot be read.' % reg)
        return data[0]

    def is_equal_to(self, a, b):
        if float(a) != float(b):
            raise AssertionError('%s != %s' % (a, b))

    def is_less_then(self, a, b):
        if float(a) >= float(b):
            raise AssertionError('%s >= %s' % (a, value))

    def is_more_then(self, a, b):
        if float(a) <= float(b):
            raise AssertionError('%s <= %s' % (a, b))

    def is_between(self, value, minVal, maxVal):
        result = True if float(minVal) <= float(value) <= float(maxVal) else False
        if not result:
            raise AssertionError('%s not in range [%s, %s]' % (value, minVal, maxVal))

    def wait_for(self, t):
        time.sleep(float(t))

    def should_cause_error(self, expression):
        """Verifies that calculating the given ``expression`` causes an error.

        The error message is returned and can be verified using, for example,
        `Should Be Equal` or other keywords in `BuiltIn` library.

        Examples:
        | Should Cause Error | invalid            |                   |
        | ${error} =         | Should Cause Error | 1 / 0             |
        | Should Be Equal    | ${error}           | Division by zero. |
        """
        try:
            self.push_buttons(expression)
        except CalculationError as err:
            return str(err)
        else:
            raise AssertionError("'%s' should have caused an error."
                                 % expression)

class CalculationError(Exception):
    pass
