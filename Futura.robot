*** Settings ***
Library       JltModbusTcp.py
Library       PyKeywords.py


*** Keywords ***

"${value}" is between ${minValue} and ${maxValue}
    #Log  ${value}  ${minValue}  ${maxValue}
    is between    ${value}  ${minValue}  ${maxValue}

wait for ${time} seconds
    wait for   ${time}

${value1} is ${mul} times greater than ${value2}
    is_greater_than_times    ${value1} ${value2} ${mul}


"${value1}" is equal to "${value2}"
    is_equal_to    ${value1}    ${value2}

# Testcase 1

indoor temeprature
    ${indoorTemp} =   temp_indoor
    log  ${indoorTemp}
    [Return]  ${indoorTemp}

indoor temperature is bellow setpoint by ${offset} degree
    ${indoorTemp} =  indoor temeprature
    writeFormatedHolding    cfg_temp_set   ${indoorTemp} + ${offset}

heating function is ${enable}
    Run Keyword If    '${enable}' == 'enabled'      writeFormatedHolding  cfg_heating_enable  1
    Run Keyword If    '${enable}' == 'disabled'     writeFormatedHolding  cfg_heating_enable  0
    wait for   10.0

current heating power
    ${heatingPower} =  readFormatedInput  fut_heating_power
    log  ${heatingPower}
    [Return]  ${heatingPower}


heating power is ${power} watts
    ${heatPower} =    current heating power
    is_equal_to    ${heatPower}   ${power}


# Testcase 2
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
    wait for   10.0


start overpreasure for ${seconds} seconds
    writeFormatedHolding   func_overpressure_tm   ${seconds}
    # Wait a moment till the engines rpm is stabilized
    wait for  15.0


overpreasure function is ${enable}
    Run Keyword If    '${enable}' == 'enabled'      start overpreasure for 60 seconds
    Run Keyword If    '${enable}' == 'disabled'     start overpreasure for 0 seconds


# Testcase 2
boost function has been started for ${minutes} minutes
    ${seconds} =   evaluate   ${minutes} * ${60}
    writeFormatedHolding   func_overpressure_tm   ${seconds}
    # Wait a moment till the engines RPM is stabilized
    wait for  15.0

fan rpm
    # Compute just an average of supply and exhast rpms
    ${supplyRpm} =  readFormatedHolding  fut_fan_rpm_supply
    ${exhaustRpm} =  readFormatedHolding  fut_fan_rpm_exhaust
    ${fanRpm} =   evaluate  (${supplyRpm} + ${exhaustRpm}) / ${2}
    log  ${fanRpm}
    [Return]  ${fanRpm}