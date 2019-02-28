*** Settings ***
Library       futuraMbRegisters.py
Library       JltModbusTcp.py        192.168.23.216      502
Library       Auxiliaries.py


*** Keywords ***

"${value}" is between ${minValue} and ${maxValue}
    #Log  ${value}  ${minValue}  ${maxValue}
    is between    ${value}  ${minValue}  ${maxValue}

wait for ${time} seconds
    wait for   ${time}

počkej ${time} sekund
    wait for   ${time}

fan pwm ${value1} is ${mul} times greater than ${value2}
    ${pwm1} =   readFormatedHolding  fut_fan_pwm_${value1}
    ${pwm2} =   readFormatedHolding  fut_fan_pwm_${value2}
    is_greater_than_times    ${pwm2}   ${pwm1}   ${mul}


"${value1}" is equal to "${value2}"
    is_equal_to    ${value1}    ${value2}

# Check heating power

indoor temperature
    ${indoorTemp} =   temp_indoor
    log  ${indoorTemp}
    [Return]  ${indoorTemp}

indoor temperature is bellow setpoint by ${offset} degree
    ${indoorTemp} =  readFormatedInput    fut_temp_indoor
    writeFormatedHolding    cfg_temp_set   ${indoorTemp} + ${offset}

heating function is ${enable}
    Run Keyword If    '${enable}' == 'enabled'      writeFormatedHolding  cfg_heating_enable  1
    Run Keyword If    '${enable}' == 'disabled'     writeFormatedHolding  cfg_heating_enable  0
    wait for 30.0 seconds

current heating power
    ${heatingPower} =  readFormatedInput  fut_heating_power
    log  ${heatingPower}
    [Return]  ${heatingPower}


heating power is ${power} watts
    ${heatPower} =    current heating power
    is_equal_to    ${heatPower}   ${power}


# Check overpreasure
supply fan rmp
    ${supplyRpm} =  readFormatedHolding  fut_fan_rpm_supply
    log  ${supplyRpm}
    [Return]  ${supplyRpm}

exhaust fan rpm
    ${exhaustRpm} =  readFormatedHolding  fut_fan_rpm_exhaust
    log  ${exhaustRpm}
    [Return]  ${exhaustRpm}


ventilation is set to level ${level}
    writeFormatedHolding  func_ventilation  ${level}
    # Wait a moment till the engines rpmd is stabilized
    wait for 10.0 seconds

ventilace je nastavena na úroveň ${úroveň}
    writeFormatedHolding  func_ventilation  ${úroveň}
    # Wait a moment till the engines rpmd is stabilized
    wait for   10.0

start overpreasure for ${seconds} seconds
    writeFormatedHolding   func_overpressure_tm   ${seconds}
    # Wait a moment till the engines rpm is stabilized
    wait for  10.0


overpreasure function is ${enable} for ${seconds} seconds
    Run Keyword If    '${enable}' == 'enabled'      start overpreasure for ${seconds} seconds
    Run Keyword If    '${enable}' == 'disabled'     start overpreasure for 0 seconds


# Check boost
boost function has been started for ${seconds} seconds
    writeFormatedHolding   func_boost_tm   ${seconds}
    # Wait a moment till the engines RPM is stabilized
    wait for  15.0

funkce boost je aktivována na ${seconds} sekund
    writeFormatedHolding   func_boost_tm   ${seconds}
    # Wait a moment till the engines RPM is stabilized
    wait for  15.0

fan speed is between ${low} and ${high} rpm
    ${supplyRpm} =  readFormatedHolding  fut_fan_rpm_supply
    ${exhaustRpm} =  readFormatedHolding  fut_fan_rpm_exhaust
    ${currentRrmp} =   evaluate  (${supplyRpm} + ${exhaustRpm}) / ${2}
    log  ${currentRrmp}
    is between    ${currentRrmp}  ${low}  ${high}

rychlost ventilátorů by měla být mezi ${low} a ${high} rpm
    ${supplyRpm} =  readFormatedHolding  fut_fan_rpm_supply
    ${exhaustRpm} =  readFormatedHolding  fut_fan_rpm_exhaust
    ${currentRrmp} =   evaluate  (${supplyRpm} + ${exhaustRpm}) / ${2}
    log  ${currentRrmp}
    is between    ${currentRrmp}  ${low}  ${high}

fan rpm
    # Compute just an average of supply and exhast rpms
    ${supplyRpm} =  readFormatedHolding  fut_fan_rpm_supply
    ${exhaustRpm} =  readFormatedHolding  fut_fan_rpm_exhaust
    ${fanRpm} =   evaluate  (${supplyRpm} + ${exhaustRpm}) / ${2}
    log  ${fanRpm}
    [Return]  ${fanRpm}


# Check bypass
bypass function is ${enable}
    Run Keyword If    '${enable}' == 'enabled'      writeFormatedHolding  cfg_bypass_enable  1
    Run Keyword If    '${enable}' == 'disabled'     writeFormatedHolding  cfg_bypass_enable  0
    wait for 40 seconds


temperature ${value1} and ${value2} differs by up to ${diff} degree
    ${temp1} =   readFormatedInput    fut_temp_${value1}
    ${temp2} =   readFormatedInput    fut_temp_${value2}
    log  ${temp1}
    log  ${temp2}
    log  ${diff}
    values differs by    ${temp1}   ${temp2}   ${diff}



ambient temperature
    ${ambientTemp} =   temp_ambient
    log  ${ambientTemp}
    [Return]  ${ambientTemp}

fresh temperature
    ${ambientTemp} =   temp_fresh
    log  ${ambientTemp}

    [Return]  ${ambientTemp}

# Check circulation
circulation function is started for ${seconds} seconds
    writeFormatedHolding   func_circulation_tm   ${seconds}
    # Wait a moment till the flaps has been moved to correct posiotion
    wait for  20.0