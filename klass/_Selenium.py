# -*- coding: utf-8 -*-
''' @ /klass/Selenium.py '''

# Import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SeleniumKlass:
  ''' Class [ SeleniumKlass ] '''

  def __init__(self, url):
    self.url = url
    self.driver = webdriver.Firefox()
    self.keys = Keys

  def __del__(self):
    print 'Selenium deleted.'

  def __str__(self):
    return 'This is Selenium.'

  def getScreenShot(self, imgPath):
    ''' Class [ SeleniumKlass ] - getScreenShot(imgPathStr) => Get Screenshot '''
    self.driver.save_screenshot(imgPath)

  def getDriver(self):
    ''' Class [ SeleniumKlass ] - getDriver(none) => Get self.driver '''
    return self.driver

  def bind(self):
    ''' Class [ SeleniumKlass ] - bind(none) => Access [ Override ] '''
    driver = self.getDriver()
    driver.get(self.url)