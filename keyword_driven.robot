*** Settings ***
Documentation     Futura test cases using the keyword-driven testing approach.
Resource          Futura.robot

*** Variables ***
${modbusClient} =  192.168.23.77

*** Test Cases ***
Check heating pwm
    modbus client ${modbusClient} has been opened
    enable heating
    ${cfg_heating_enable} =   heating enabled
    Should Be Equal  ${cfg_heating_enable}  ${1}
    ${indoorTemp} =  indoor temeprature
    ${setpoint} =  setpoint
    ${expectedPwm} =  evaluate  (${setpoint}-${indoorTemp}) * ${100} / ${30}
    ${heatingPwm} =  heating pwm
    ${heatingPwm} is between 0 and 100
    run keyword if  ${expectedPwm} > ${100}  ${expectedPwm} =  ${100}
    run keyword if  ${expectedPwm} < ${0}  ${expectedPwm} =  ${0}
    ${expectedMinPwm} =  evaluate  ${expectedPwm} - ${10}
    ${expectedManPwm} =  evaluate  ${expectedPwm} + ${10}
    ${heatingPwm} is between ${expectedMinPwm} and ${expectedManPwm}
    indoor temeprature is between 0 and 100
    disable heating

Check overpreasure enabled
    modbus client ${modbusClient} has been opened
    # Now enable the overpreasure and check increasing the PWM duty of the supply engine
    start overpreasure for 60 seconds
    ${supplyPwm} =  supply fan pwm
    ${exhaustPwm} =  exhaust fan pwm
    # Use default overpreasure ration
    ${temp} =  evaluate  ${exhaustPwm} * 1.1
    # Round the given number
    ${expectedSupplyPwm} =  Convert To Number  ${temp}  0
    Should Be Equal  ${expectedSupplyPwm}  ${supplyPwm}

Check overpreasure disabled
    modbus client ${modbusClient} has been opened
    # Disable overpreasure and check the engines has same PWM duty
    start overpreasure for 0 seconds
    ${supplyPwm} =  supply fan pwm
    ${exhaustPwm} =  exhaust fan pwm
    Should Be Equal  ${supplyPwm}  ${exhaustPwm}

Check antiradon enabled
    modbus client ${modbusClient} has been opened
    # Now enable the overpreasure and check increasing the PWM duty of the supply engine
    start antiradon protection
    ${supplyPwm} =  supply fan pwm
    ${exhaustPwm} =  exhaust fan pwm
    # Use default antiradon ration
    ${temp} =  evaluate  ${exhaustPwm} * 1.05
    ${expectedSupplyPwm} =  Convert To Number  ${temp}  0
    Should Be Equal  ${expectedSupplyPwm}  ${supplyPwm}

Check antiradon disabled
    modbus client ${modbusClient} has been opened
    # Disable overpreasure and check the engines has same PWM duty
    stop antiradon protection
    ${supplyPwm} =  supply fan pwm
    ${exhaustPwm} =  exhaust fan pwm
    Should Be Equal  ${supplyPwm}  ${exhaustPwm}






