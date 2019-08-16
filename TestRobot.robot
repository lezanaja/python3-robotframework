*** Settings ***
Library           AwareLibrary

*** Test Cases ***
01
    ${result}    Get Hello World
    Log    ${result}
