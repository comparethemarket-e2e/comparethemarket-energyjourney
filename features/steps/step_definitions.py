from behave import *
from page import get_page
from robber import expect


@given("a user navigates to the '{page_name}'")
def step_impl(context, page_name):
  page_class = get_page(page_name)
  context.page = page_class(context.driver)
  context.page.go()
  
@when("a user enters '{input_text}' into the '{element_name}'")
def step_impl(context, input_text, element_name):
  element = context.page.get_element(element_name)
  element.set(input_text)

@step("a user clicks on the '{element_name}'")
def step_impl(context, element_name):
  element = context.page.get_element(element_name)
  element.click()

@then("the '{element_name}' should be visible")
def step_impl(context, element_name):
  element = context.page.get_element(element_name)
  expect(element.is_visible()).to.be.true()

@when("a user selects '{item_name}' from the '{element_name}'")
def step_impl(context, item_name, element_name):
  collection = context.page.get_element(element_name)
  element = collection.set(item_name)

@then("'{item_name}' should be selected in the '{element_name}'")
def step_impl(context, item_name, element_name):
  collection = context.page.get_element(element_name)
  element = collection.get_selected()
  expect(element.text).to.contain(item_name)

@then("they should arrive on the '{page_name}'")
def step_impl(context, page_name):
  page_class = get_page(page_name)
  context.page = page_class(context.driver)
  expect(context.page.is_loaded()).to.be.true()

@then("the '{element_name}' should contain '{text}'")
def step_impl(context, element_name, text):
  element = context.page.get_element(element_name)
  expect(element.text).to.eq(text)

@given("a user has filled in supplier information")
def step_impl(context):
  context.execute_steps(u"""
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
    """
  )

@given("a user has filled in information about their supplier and energy bill")
def step_impl(context):
  context.execute_steps(u"""
    Given a user has filled in supplier information
    When a user enters '200' into the 'current spend field'
    And a user clicks on the 'next button'
    Then they should arrive on the 'your details page'
    """
  )