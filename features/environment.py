from appium import webdriver
from app.application import Application

def before_scenario(context, scenario):
    context.driver = webdriver.Remote("http://127.0.0.1:4723",
                                      desired_capabilities={'platformName': 'Android',
                                                            'platformVersion': '11.0',
                                                            'deviceName': 'ZY22DHFVBM',
                                                            'automationName': 'UiAutomator2',
                                                            'app': 'path/to/alquiler.apk',
                                                            'appPackage': 'com.alquiler',
                                                            "appWaitActivity": 'com.alquiler.appindex.presentation.activity.SearchActivity'
                                                            })

    context.driver.implicitly_wait(60)
 
    context.app = Application(context.driver)

def after_scenario(context, scenario):
    context.driver.quit()
