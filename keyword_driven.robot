*** Settings ***
Documentation     Example test cases using the keyword-driven testing approach.
...
...               All tests contain a workflow constructed from keywords in
...               ``CalculatorLibrary.py``. Creating new tests or editing
...               existing is easy even for people without programming skills.
...
...               The _keyword-driven_ appoach works well for normal test
...               automation, but the _gherkin_ style might be even better
...               if also business people need to understand tests. If the
...               same workflow needs to repeated multiple times, it is best
...               to use to the _data-driven_ approach.
Resource          Futura.robot

*** Variables ***
${modbusClient} =  192.168.23.77

*** Test Cases ***
Check heating pwm
    modbus client ${modbusClient} has been opened
    ${cfg_heating_enable} =   heating enable
    ${indoorTemp} =  indoor temeprature
    ${setpoint} =  setpoint
    ${expectedPwm} =  evaluate  (${setpoint}-${indoorTemp})*100/30
    ${heatingPwm} =  heating pwm
    ${heatingPwm} is between 0 and 100
    run keyword if  ${expectedPwm}>100  ${expectedPwm} =  100
    run keyword if  ${expectedPwm} < 0  ${expectedPwm} =  0
    ${expectedMinPwm} =  evaluate  ${expectedPwm}-10
    ${expectedManPwm} =  evaluate  ${expectedPwm}+10
    run keyword if  ${cfg_heating_enable}==1  ${heatingPwm} is between ${expectedMinPwm} and ${expectedManPwm}


Check overpreasure
    modbus client ${modbusClient} has been opened
    ${cfg_heating_enable} =   heating enable
    ${indoorTemp} =  indoor temeprature
    ${setpoint} =  setpoint
    ${expectedPwm} =  evaluate  (${setpoint}-${indoorTemp})*100/30
    ${heatingPwm} =  heating pwm
    ${heatingPwm} is between 0 and 100
    run keyword if  ${expectedPwm}>100  ${expectedPwm} =  100
    run keyword if  ${expectedPwm} < 0  ${expectedPwm} =  0
    ${expectedMinPwm} =  evaluate  ${expectedPwm}-10
    ${expectedManPwm} =  evaluate  ${expectedPwm}+10
    run keyword if  ${cfg_heating_enable}==1  ${heatingPwm} is between ${expectedMinPwm} and ${expectedManPwm}




