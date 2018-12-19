from pyModbusTCP.client import ModbusClient
import struct

class FuturaLibrary(object):
    def __init__(self):
        self._mbClient = None
        self._justReadReg = None
    
    def open_client(self, hostAddr = 'localhost'):
        if self._mbClient:
            raise AssertionError('Modbus client is alredy opened!')
        self._mbClient = ModbusClient(host=hostAddr, port=502, auto_open=True)
        
    def open_client(self, hostAddr = 'localhost'):
        if not self._mbClient:
            raise AssertionError('Modbus client is not opened!')
        self._mbClient = ModbusClient(host=hostAddr, port=502, auto_open=True)

    def read_holding_register_short(self, reg):
        data = self._mbClient.read_holding_registers(reg, 1)
        if data:
            self._justReadReg = data[0]
        else:
            print("read error")

    def read_holding_register_long(self, reg):
        data = self._mbClient.read_holding_registers(reg, 2)
        if data:
            self._justReadReg = struct.unpack('H'*2, data)
        else:
            print("read error")


    def result_should_be(self, expected):
        """Verifies that the current result is ``expected``.

        Example:
        | Push Buttons     | 1 + 2 = |
        | Result Should Be | 3       |
        """
        if self._result != expected:
            raise AssertionError('%s != %s' % (self._result, expected))

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


data = [2, 2]
print(struct.unpack('HH', data[0], data[1]))