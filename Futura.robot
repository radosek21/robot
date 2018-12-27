*** Settings ***
Library       FuturaLibrary.py


*** Keywords ***
# Low level keywords
modbus client ${client} has been opened
    open client  ${client}

user reads the register ${addr}
    ${value} =  read holding register  ${addr}
    Return From Keyword  ${value}

user reads the input register ${addr}
    ${value} =  read input register  ${addr}
    Return From Keyword  ${value}

result is equal to ${value}
    result is equal to   ${value}

result is less then ${value}
    result is less then   ${value}

result is more then ${value}
    result is more then   ${value}

${value} is between ${minValue} and ${maxValue}
    #Log  ${value}  ${minValue}  ${maxValue}
    is between    ${value}  ${minValue}  ${maxValue}

wait for ${time} seconds
    wait for   ${time}

# High level keywords
outdoor temeprature
    ${outdoorTemp} =  read input named register  temp_ambient
    log  ${outdoorTemp}
    Return From Keyword  ${outdoorTemp}

waste temeprature
    ${wasteTemp} =  read input named register  temp_waste
    log  ${wasteTemp}
    Return From Keyword  ${wasteTemp}

fresh temeprature
    ${freshTemp} =  read input named register  temp_fresh
    log  ${freshTemp}
    Return From Keyword  ${freshTemp}

indoor temeprature
    ${indoorTemp} =  read input named register  temp_indoor
    log  ${indoorTemp}
    Return From Keyword  ${indoorTemp}

heating pwm
    ${heatingPwm} =  read holding named register  fut_heating_pwm
    log  ${heatingPwm}
    Return From Keyword  ${heatingPwm}

setpoint
    ${setpoint} =  read holding named register  cfg_temp_set
    log  ${setpoint}
    Return From Keyword  ${setpoint}