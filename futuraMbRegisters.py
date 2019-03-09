# -*- coding: utf-8 -*-

futuraInputRegisters = {
'fut_temp_ambient': {'regNr': 30, 'size': 1, 'format': 'SINT', 'power': 10, 'min': None, 'max': None},
'fut_temp_fresh': {'regNr': 31, 'size': 1, 'format': 'SINT', 'power': 10, 'min': None, 'max': None},
'fut_temp_indoor': {'regNr': 32, 'size': 1, 'format': 'SINT', 'power': 10, 'min': None, 'max': None},
'fut_temp_waste': {'regNr': 33, 'size': 1, 'format': 'SINT', 'power': 10, 'min': None, 'max': None},
'fut_heating_power': {'regNr': 43, 'size': 1, 'format': 'UINT', 'power': '', 'min': '', 'max': ''},
}

futuraHoldingRegisters = {
'func_ventilation': {'regNr': 0, 'size': 1, 'format': 'UINT', 'power': None, 'min': 0, 'max': 6},
'func_boost_tm': {'regNr': 1, 'size': 1, 'format': 'UINT', 'power': None, 'min': 0, 'max': 7200},
'func_circulation_tm': {'regNr': 2, 'size': 1, 'format': 'UINT', 'power': None, 'min': 0, 'max': 7200},
'func_overpressure_tm': {'regNr': 3, 'size': 1, 'format': 'UINT', 'power': None, 'min': 0, 'max': 7200},
'cfg_temp_set': {'regNr': 10, 'size': 1, 'format': 'UINT', 'power': 10, 'min': 50, 'max': 300},
'cfg_bypass_enable': {'regNr': 14, 'size': 1, 'format': 'UINT', 'power': None, 'min': 0, 'max': 255},
'cfg_heating_enable': {'regNr': 15, 'size': 1, 'format': 'UINT', 'power': None, 'min': 0, 'max': 255},
'fut_fan_pwm_supply': {'regNr': 904, 'size': 1, 'format': 'UINT', 'power': None, 'min': 0, 'max': 100},
'fut_fan_pwm_exhaust': {'regNr': 905, 'size': 1, 'format': 'UINT', 'power': None, 'min': 0, 'max': 100},
'fut_heating_pwm': {'regNr': 910, 'size': 1, 'format': 'UINT', 'power': None, 'min': 0, 'max': 100},
'fut_fan_rpm_supply': {'regNr': 939, 'size': 1, 'format': 'UINT', 'power': None, 'min': None, 'max': None},
'fut_fan_rpm_exhaust': {'regNr': 940, 'size': 1, 'format': 'UINT', 'power': None, 'min': None, 'max': None},
}

