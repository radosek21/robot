*** Settings ***
Documentation     Example test case using the gherkin syntax.
Resource          Futura.robot



*** Test Cases ***
Check bypass
    Given ventilation is set to level 2
    When bypass function is enabled
    Then temperature ambient and fresh differs by up to 2.0 degree
    And bypass function is disabled

Check boost
    Given ventilation is set to level 1
    When boost function has been started for 20 seconds
    Then fan speed is between 1900 and 2100 rpm
    And wait for 10 seconds

Check circulation
    Given ventilation is set to level 2
    When circulation function is started for 25 seconds
    Then temperature ambient and waste differs by up to 0.5 degree

Check overpreasure
    Given ventilation is set to level 5
    When overpreasure function is enabled for 15 seconds
    Then fan pwm supply is 1.1 times greater than exhaust
    And wait for 10 seconds

Check heating power
    Given indoor temperature is bellow setpoint by 3.5 degree
    When ventilation is set to level 2
    And heating function is enabled
    Then heating power is 350 watts
    And heating function is disabled

