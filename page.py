from selenium.webdriver.common.by import By
from element import ListElement, Element

YOUR_SUPPLIER_URL = "https://energy.comparethemarket.com/energy/v2/?AFFCLIE=TST"


def get_page(page_name):
  pages = {
    'your supplier page': YourSupplierPage,
    'your energy page': YourEnergyPage,
    'your details page': YourDetailsPage,
    'your results page': YourResultsPage
  }
  return pages[page_name]


class BasePage(object):
  def __init__(self, driver, url=None):
    self.driver = driver
    self.url = url

  def go(self):
    self.driver.get(self.url)

  def get_element(self, name):
    return getattr(self, name.replace(" ", "_"))

  def is_loaded(self):
    pass


class YourSupplierLocators(object):
  YOUR_POSTCODE = (By.ID, 'your-postcode')
  FIND_POSTCODE_BUTTON = (By.ID, 'find-postcode')
  YOUR_SUPPLIER_FORM = (By.ID, 'yourSupplier')
  TOP_SUPPLIERS_LIST = (By.CSS_SELECTOR, '#elec-energy-suppliers-question .top-six')
  HAS_NO_BILL_BUTTON = (By.CLASS_NAME, 'have-bill-no')
  ELECTRICITY_ONLY_BUTTON = (By.CLASS_NAME, 'energy-electricity')
  NEXT_BUTTON = (By.ID, 'goto-your-supplier-details')


class YourSupplierPage(BasePage):
  def __init__(self, driver, url=YOUR_SUPPLIER_URL):
    super(YourSupplierPage, self).__init__(driver, url)

    self.postcode_field = Element(driver, YourSupplierLocators.YOUR_POSTCODE)
    self.find_postcode_button = Element(driver, YourSupplierLocators.FIND_POSTCODE_BUTTON)
    self.your_supplier_form = Element(driver, YourSupplierLocators.YOUR_SUPPLIER_FORM)
    self.top_suppliers_list = ListElement(driver, YourSupplierLocators.TOP_SUPPLIERS_LIST)
    self.has_no_bill_button = Element(driver, YourSupplierLocators.HAS_NO_BILL_BUTTON)
    self.electricity_only_button = Element(driver, YourSupplierLocators.ELECTRICITY_ONLY_BUTTON)
    self.next_button = Element(driver, YourSupplierLocators.NEXT_BUTTON)


class YourEnergyLocators(object):
  TITLE = (By.CLASS_NAME, 'main-heading')
  CURRENT_SPEND_FIELD = (By.ID, 'electricity-current-spend')
  NEXT_BUTTON = (By.ID, 'goto-your-energy')


class YourEnergyPage(BasePage):
  def __init__(self, driver, url=None):
    super(YourEnergyPage, self).__init__(driver, url)

    self.title = Element(driver, YourEnergyLocators.TITLE)
    self.current_spend_field = Element(driver, YourEnergyLocators.CURRENT_SPEND_FIELD)
    self.next_button = Element(driver, YourEnergyLocators.NEXT_BUTTON)

  def is_loaded(self):
    return self.title.is_visible()


class YourDetailsLocators(object):
  TITLE = (By.CLASS_NAME, 'main-heading')
  TARIFF_LIST = (By.XPATH, '//label[@data-group-name="pre-select-tariff-type"]')
  PAYMENT_TYPES = (By.XPATH, '//label[@data-group-name="pre-select-payment-type"]')
  EMAIL_FIELD = (By.ID, 'Email')
  TERMS_AND_CONDITIONS_CHECKBOX = (By.ID, 'terms-label')
  GO_TO_PRICES_BUTTON = (By.ID, 'email-submit')



class YourDetailsPage(BasePage):
  def __init__(self, driver, url=None):
    super(YourDetailsPage, self).__init__(driver, url)

    self.title = Element(driver, YourDetailsLocators.TITLE)
    self.tariff_list = ListElement(driver, YourDetailsLocators.TARIFF_LIST)
    self.payment_types = ListElement(driver, YourDetailsLocators.PAYMENT_TYPES)
    self.email_field = Element(driver, YourDetailsLocators.EMAIL_FIELD)
    self.terms_and_conditions_checkbox = Element(driver, YourDetailsLocators.TERMS_AND_CONDITIONS_CHECKBOX)
    self.go_to_prices_button = Element(driver, YourDetailsLocators.GO_TO_PRICES_BUTTON)


  def is_loaded(self):
    return self.title.is_visible()


class YourResultsLocators(object):
  TITLE = (By.CLASS_NAME, 'results-title')
  RESULTS = (By.CLASS_NAME, 'list-view-row')


class YourResultsPage(BasePage):
  def __init__(self, driver, url=None):
    super(YourResultsPage, self).__init__(driver, url)

    self.title = Element(driver, YourResultsLocators.TITLE)
    self.results = ListElement(driver, YourResultsLocators.RESULTS)


  def is_loaded(self):
    return self.title.is_visible()
