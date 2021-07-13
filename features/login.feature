Feature: User is able to login to Hudl.com

    Scenario: User is able to login with valid email and password
        Given user has navigated to Hudl.com
        And user clicks on the Login button
        When user is taken to the Login page
        And user enters their valid credentials
        And user clicks the Login button
        Then user is taken to their dashboard

    Scenario: User is unable to login with valid email and invalid password
        Given user has navigated to Hudl.com
        And user clicks on the Login button
        When user is taken to the Login page
        And user enters a valid email address
        And user enters an invalid password
        When user clicks the Login button
        Then user is presented with a "We didn't recognize that email and/or password. Need help?" error message
        And user is unable to click the Login button

    Scenario: User is unable to login without providing an email and password
        Given user has navigated to Hudl.com
        And user clicks on the Login button
        When user is taken to the Login page
        And user clicks the Login button
        Then user is presented with a "We didn't recognize that email and/or password. Need help?" error message
        And user is unable to click the Login button 
