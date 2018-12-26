*** Settings ***
Library       FuturaLibrary.py


*** Keywords ***
# Low level keywords
modbus has been opened
    open client

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
    ${outTemp} =  read holding register  12
    log  ${outTemp}
    Return From Keyword  ${outTemp}

setpoint
    ${setpoint} =  read holding register  12
    log  ${setpoint}
    Return From Keyword  ${setpoint}