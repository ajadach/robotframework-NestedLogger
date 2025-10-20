*** Settings ***
Documentation    Test cases for NestedLogger library
Library          python/ExampleTestLib.py

*** Test Cases ***
Test Basic Keyword
    [Documentation]    Test a basic keyword from the example library
    ${result}=    Do Something
    Should Be Equal    ${result}    Did something!

Test Nested Logging
    [Documentation]    Test nested keyword logging functionality
    Do Something With My Logger    Parameter1    Value1    Parameter2    Value2    Parameter3    Value3

*** Keywords ***
# Add custom keywords here if needed
