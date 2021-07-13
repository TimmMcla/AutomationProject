# Automation Prototype

## This is a prototype to run up a local automation framework to test a website's login functionality using Python, Selenium, and Behave.

### I ran into some problems while trying to get this prototype up and running...
  1. Prior to this experiment, my knowledge of Python was extremely limited.
  2. I did not understand the intricacies that behave revoles around.  

### I will be continuing to bring this project to a runnable state. Currently, it opens a web site successfully.

### Setup instructions:

Application dependencies:

   Python 3.7.3, selenium, behave
  
  - I ran this within a virtual environment. 
  
Application layer:

1. Open helper/fixtures.py and put your local chromedriver's path within the quotes.
2. Create a setup.cfg file in the main directory and paste this into the file:

            [ Environment ]

            Browser = chrome


## Improvements coming soon:
 - Extract the hardcoded setup values to a base configuration file. 
 - Incorporate openpyxl and extract all test data to spreadsheets.
 - Have the page objects handle the driver instance so that the step definitions are easily readable.
 - Finish the test cases and have it complete the scenario runs.
 - Expand the browsers tested to include the major versions of Edge, Firefox, and Safari
