*** Settings ***
Documentation     Example test case using the gherkin syntax.
Resource          Futura.robot



*** Test Cases ***
Addition
    Given calculator has been cleared
    When user types "1 + 1"
    and user pushes equals
    Then result is "2"

