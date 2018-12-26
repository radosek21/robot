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

*** Test Cases ***

Check version
    modbus has been opened
#    user reads the input register 2
#    result is equal to 15
    ${outdoor} =  outdoor temeprature
    ${setpoint} =  setpoint
    ${outdoor} is between ${setpoint-0.2} and ${setpoint+0.1}
