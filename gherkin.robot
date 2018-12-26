*** Settings ***
Documentation     Example test case using the gherkin syntax.
Resource          Futura.robot



*** Test Cases ***
Fist test
    Given modbus has been opened
    When user reads the register 1
    Then result is between 1.0 and 9.9

advanced test
    Given modbus has been opened
    When user reads the register 1
    Then outdoor temeprature is between 10 and 20