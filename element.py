from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

TIMEOUT = 15


def coerce_to_bool(wrapped_function):
  def wrapper(self):
    try:
      wrapped_function(self)
      return True
    except TimeoutException:
      return False

  return wrapper


class BaseElement(object):
  def __init__(self, driver, locator):
    self.driver = driver
    self.locator = locator

  def _wait_for(self, expected_condition):
    return WebDriverWait(self.driver, TIMEOUT).until(
      expected_condition(self.locator)
    )

  def get(self):
    return self._wait_for_presence()

  def _wait_for_presence(self):
    raise NotImplementedError()


class Element(BaseElement):

  @property
  def text(self):
    return self.get().text

  def click(self):
    return self.get().click()

  def set(self, text):
    return self.get().send_keys(text)

  def _wait_for_visibility(self):
    return self._wait_for(
      EC.visibility_of_element_located
    )

  def _wait_for_presence(self):
    return self._wait_for(
      EC.presence_of_element_located
    )

  @coerce_to_bool
  def is_visible(self):
    return self._wait_for_visibility()


class ListElement(BaseElement):

  def _wait_for_presence(self):
    return self._wait_for(
      EC.presence_of_all_elements_located
    )

  def set(self, text):
    selected = self.get_item(text)
    selected.click()

  @coerce_to_bool
  def is_present(self):
    return self._wait_for_presence()

  def is_visible(self):
    els = self._wait_for_presence()
    return all([el.is_displayed() for el in els])

  def filter_collection_by(self, condition):
    els = self.get()
    matches = filter(condition, els)
    return matches

  def get_item(self, text):
    element_contains_text = lambda el: text in el.text
    return self.filter_collection_by(element_contains_text)[0]

  def get_selected(self):
    element_is_selected = lambda el: "checked" in el.get_attribute("class")
    return self.filter_collection_by(element_is_selected)[0]

  def __getitem__(self, index):
    return self.get()[index]

  def __len__(self):
    return len(self.get())
