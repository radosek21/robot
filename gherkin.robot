*** Settings ***
Documentation     Example test case using the gherkin syntax.
Resource          Futura.robot



*** Test Cases ***
Check boost
    Given ventilation is set to level 1
    When boost function has been started for 1 minutes
    Then supply fan rpm is between 1000 and 2000 rpm


Check heating power
    Given indoor temperature is bellow setpoint by 3 degree
    When ventilation is set to level 2
    And heating function is enabled
    Then heating power is 350 watts


Check overpreasure
    Given ventilation is set to level 3
    When overpreasure function is enabled
    Then supply fan rpm is 1.1 times greater than exhaust fan rpm
