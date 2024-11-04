import  os
from selenium.webdriver import ChromeOptions
from selenium   import  webdriver

username = os.environ.get('BROWSERSTACK_USERNAME')
accessKey = os.environ.get('BROWSERSTACK_ACCESS_KEY')
buildName = os.environ.get('BROWSERSTACK_BUILD_NAME')
local = os.environ.get('BROWSERSTACK_LOCAL')
localIdentifier = os.environ.get('BROWSERSTACK_LOCAL_IDENTIFIER')

bstack_options = {
    "os" : "Windows",
    "osVersion" : "10",
    "sessionName" : "BStack Build Name: " + buildName,
    "local": local,
    "localIdentifier": localIdentifier,
    "seleniumVersion" : "4.0.0",
    "userName": username,
    "accessKey": accessKey
}
options = ChromeOptions()
options.set_capability('bstack:options', bstack_options)
driver = webdriver.Remote(
    command_executor="https://hub.browserstack.com/wd/hub",
    options=options)
   