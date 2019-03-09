*** Settings ***
Documentation     Example test case using the gherkin syntax.
Resource          Keywords.robot



*** Test Cases ***
Check bypass
    Given ventilation is set to level 2
    

Check boost
    Given ventilation is set to level 1
    

Check circulation
    Given ventilation is set to level 2
    

Check overpreasure
    Given ventilation is set to level 5
    

Check heating power
    Given ventilation is set to level 1
    

