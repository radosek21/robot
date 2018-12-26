from pyModbusTCP.client import ModbusClient
import time
import struct

class FuturaLibrary(object):
    def __init__(self):
        self._mbClient = None
        self._justReadReg = None
    
    def open_client(self, hostAddr = 'localhost'):
        if self._mbClient:
            raise AssertionError('Modbus client is already opened!')
        self._mbClient = ModbusClient(host=hostAddr, port=502, auto_open=True)
        if not self._mbClient:
            raise AssertionError('Modbus client cannot be opened.')

    def read_holding_register(self, reg):
        #data = self._mbClient.read_holding_registers(int(reg), 1)
        #if data:
        #    self._justReadReg = data[0]
        #else:
        #    raise AssertionError('Holding register %s cannot be read.' % reg)
        self._justReadReg = 10
        return self._justReadReg

    def read_input_register(self, reg):
        data = self._mbClient.read_input_registers(int(reg), 1)
        if data:
            self._justReadReg = data[0]
        else:
            raise AssertionError('Input register %s cannot be read.' % reg)
        return self._justReadReg

    def read_holding_register_long(self, reg):
        data = self._mbClient.read_holding_registers(reg, 2)
        if data:
            self._justReadReg = data[0] | ( data[1] << 16 )
        else:
            raise AssertionError('Holding register %s cannot be read.' % reg)
        return self._justReadReg

    def result_is_equal_to(self, expected):
        if self._justReadReg != float(expected):
            raise AssertionError('%s != %s' % (self._justReadReg, expected))

    def result_is_less_then(self, value):
        if self._justReadReg >= float(value):
            raise AssertionError('%s >= %s' % (self._justReadReg, value))

    def result_is_more_then(self, value):
        if self._justReadReg <= float(value):
            raise AssertionError('%s <= %s' % (self._justReadReg, value))

    def result_is_between(self, value1, value2):
        if self._justReadReg < float(value1) or self._justReadReg > float(value2):
            raise AssertionError('%s not in range [%s, %s]' % (self._justReadReg, value1, value2))

    def is_between(self, value, minVal, maxVal):
        result = True if float(minVal) <= float(value) <= float(maxVal) else False
        if not result:
            raise AssertionError('%s not in range [%s, %s]' % (self._justReadReg, minVal, maxVal))

    def wait_for(self, t):
        time.sleep(t)

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
