from pyModbusTCP.server import ModbusServer

if __name__ == '__main__':
    server = ModbusServer(host='localhost', port=502)
    server.start()
