Feature: Energy journey

  Scenario: Filling in supplier information
    Given a user navigates to the 'your supplier page'
    When a user enters 'PE2 6YS' into the 'postcode field'
    And a user clicks on the 'find postcode button'
    And a user clicks on the 'has no bill button'
    And a user clicks on the 'electricity only button'
    Then the 'your supplier form' should be visible
    When a user selects 'EDF Energy' from the 'top suppliers list'
    Then 'EDF Energy' should be selected in the 'top suppliers list'
    When a user clicks on the 'next button'
    Then they should arrive on the 'your energy page'

  Scenario: Filling in the your energy page
  	Given a user has filled in supplier information
    When a user enters '200' into the 'current spend field'
    And a user clicks on the 'next button'
    Then they should arrive on the 'your details page'

  Scenario: Providing contact details and viewing results
    Given a user has filled in information about their supplier and energy bill
    When a user selects 'Fixed tariff' from the 'tariff list'
    And a user selects 'Monthly direct debit' from the 'payment types'
    And a user enters 'test@email.com' into the 'email field'
    And a user clicks on the 'terms and conditions checkbox'
    And a user clicks on the 'go to prices button'
    Then they should arrive on the 'your results page'
    And the 'results' should be visible
