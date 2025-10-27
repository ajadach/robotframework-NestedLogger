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

Test Nested Logging With Context Manager
    [Documentation]    Test nested keyword logging using context manager
    Do Something With Context Manager    Username    admin    Password    secret123    Email    admin@example.com
