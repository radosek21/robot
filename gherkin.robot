*** Settings ***
Documentation     Example test case using the gherkin syntax.
Resource          Futura.robot



*** Test Cases ***
Check heating pwm 100%
    Given indoor temperature is bellow setpoint by 3 degree
    When enable heating
    Then heating pwm is "100"


Check heating pwm 50%
    Given indoor temperature is bellow setpoint by 1.5 degree
    When enable heating
    Then heating pwm is "50"

Check overpreasure enabled
    Given overpreasure function is disabled
    When overpreasure function is enabled
    Then supply fan pwm is 1.1 times greater than exhaust fan pwm

Check antiradon enabled
    Given antiradon function is disabled
    When antiradon function is enabled
    Then supply fan pwm is 1.05 times greater than exhaust fan pwm