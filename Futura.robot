*** Settings ***
Library       FuturaLibrary.py


*** Keywords ***
# Low level keywords
modbus client ${client} has been opened
    open client  ${client}

${value} is between ${minValue} and ${maxValue}
    #Log  ${value}  ${minValue}  ${maxValue}
    is between    ${value}  ${minValue}  ${maxValue}

wait for ${time} seconds
    wait for   ${time}

# High level keywords
outdoor temeprature
    ${outdoorTemp} =  read input register  temp_ambient
    log  ${outdoorTemp}
    [Return]  ${outdoorTemp}

waste temeprature
    ${wasteTemp} =  read input register  temp_waste
    log  ${wasteTemp}
    [Return]  ${wasteTemp}

fresh temeprature
    ${freshTemp} =  read input register  temp_fresh
    log  ${freshTemp}
    [Return]  ${freshTemp}

indoor temeprature
    ${indoorTemp} =  read input register  temp_indoor
    log  ${indoorTemp}
    [Return]  ${indoorTemp}

heating pwm
    ${heatingPwm} =  read holding register  fut_heating_pwm
    log  ${heatingPwm}
    [Return]  ${heatingPwm}

heating enabled
    ${cfg_heating_enable} =  read holding register  cfg_heating_enable
    log  ${cfg_heating_enable}
    [Return]  ${cfg_heating_enable}

enable heating
    write register  cfg_heating_enable  1
    # Wait a moment till the heating PWM is stabilized
    wait for  1.0

disable heating
    write register  cfg_heating_enable  0
    # Wait a moment till the heating PWM is stabilized
    wait for  1.0

start overpreasure for ${tm} seconds
    write register  overpressure_tm  ${tm}
    # Wait a moment till the engines PWM is stabilized
    wait for  15.0

start antiradon protection
    write register  func_antiradon  1
    # Wait a moment till the engines PWM is stabilized
    wait for  15.0

stop antiradon protection
    write register  func_antiradon  0
    # Wait a moment till the engines PWM is stabilized
    wait for  15.0

supply fan pwm
    ${supplyPwm} =  read holding register  fut_fan_pwm_supply
    log  ${supplyPwm}
    [Return]  ${supplyPwm}

exhaust fan pwm
    ${exhaustPwm} =  read holding register  fut_fan_pwm_exhaust
    log  ${exhaustPwm}
    [Return]  ${exhaustPwm}

setpoint
    ${setpoint} =  read holding register  cfg_temp_set
    log  ${setpoint}
    [Return]  ${setpoint}