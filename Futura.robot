*** Settings ***
Library       JltModbusTcp.py


*** Keywords ***
# Low level keywords
modbus client ${client} has been opened
    open client  ${client}

${value} is between ${minValue} and ${maxValue}
    #Log  ${value}  ${minValue}  ${maxValue}
    is between    ${value}  ${minValue}  ${maxValue}

wait for ${time} seconds
    wait for   ${time}

${value1} is ${mul} times greater than ${value2}
    is_greater_than_times    ${value1} ${value2} ${mul}


"${value1}" is equal to "${value2}"
    is_equal_to    ${value1}    ${value2}

# High level keywords
outdoor temeprature
    ${outdoorTemp} =  readFormatedInput  temp_ambient
    log  ${outdoorTemp}
    [Return]  ${outdoorTemp}

waste temeprature
    ${wasteTemp} =  readFormatedInput  temp_waste
    log  ${wasteTemp}
    [Return]  ${wasteTemp}

fresh temeprature
    ${freshTemp} =  readFormatedInput  temp_fresh
    log  ${freshTemp}
    [Return]  ${freshTemp}

indoor temeprature
    ${indoorTemp} =   readFormatedHolding   temp_indoor
    log  ${indoorTemp}
    [Return]  ${indoorTemp}

current heating pwm
    ${heatingPwm} =  readFormatedHolding  fut_heating_pwm
    log  ${heatingPwm}
    [Return]  ${heatingPwm}

heating enabled
    ${cfg_heating_enable} =  readFormatedHolding  cfg_heating_enable
    log  ${cfg_heating_enable}
    [Return]  ${cfg_heating_enable}

enable heating
    writeFormatedHolding  cfg_heating_enable  1
    # Wait a moment till the heating PWM is stabilized
    wait for  1.0

disable heating
    writeFormatedHolding  cfg_heating_enable  0
    # Wait a moment till the heating PWM is stabilized
    wait for  1.0

start overpreasure for ${tm} seconds
    writeFormatedHolding  overpressure_tm  ${tm}
    # Wait a moment till the engines PWM is stabilized
    wait for  15.0

start antiradon protection
    write register  func_antiradon  1
    # Wait a moment till the engines PWM is stabilized
    wait for  15.0

stop antiradon protection
    writeFormatedHolding  func_antiradon  0
    # Wait a moment till the engines PWM is stabilized
    wait for  15.0

supply fan pwm
    ${supplyPwm} =  readFormatedHolding  fut_fan_pwm_supply
    log  ${supplyPwm}
    [Return]  ${supplyPwm}

exhaust fan pwm
    ${exhaustPwm} =  readFormatedHolding  fut_fan_pwm_exhaust
    log  ${exhaustPwm}
    [Return]  ${exhaustPwm}

setpoint
    ${setpoint} =  readFormatedHolding  cfg_temp_set
    log  ${setpoint}
    [Return]  ${setpoint}


indoor temperature is bellow setpoint by ${offset} degree
    ${indoorTemp} =  indoor temeprature
    writeFormatedHolding    cfg_temp_set   ${indoorTemp} + ${offset}

overpreasure function is ${enable}
    Run Keyword If    '${enable}' == 'enabled'      start overpreasure for 60 seconds
    Run Keyword If    '${enable}' == 'disabled'     start overpreasure for 0 seconds

antiradon function is ${enable}
    Run Keyword If    '${enable}' == 'enabled'      start antiradon for 60 seconds
    Run Keyword If    '${enable}' == 'disabled'     start antiradon for 0 seconds

heating pwm is "${percent}"
    ${heatPwm} =    current heating pwm
    is_equal_to    ${heatpwm}   ${percent}