from selenium.webdriver import Chrome


def before_all(context):
  context.driver = Chrome()
  context.driver.implicitly_wait(10)
  context.driver.maximize_window()

def before_scenario(context, scenario):
  context.driver.delete_all_cookies()

def after_all(context):
  context.driver.quit()