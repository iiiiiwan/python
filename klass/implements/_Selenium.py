# -*- coding: utf-8 -*-
''' @ /klass/implements/Selenium.py '''

# Import
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class SeleniumKlass:
  ''' Class [ SeleniumKlass ] '''

  def __init__(self, name, url):
    self.name    = name;
    self.url     = url;
    self.driver  = webdriver.Firefox();
    self.waiting = WebDriverWait(self.driver, 5);
    self.keys    = Keys;

  def __del__(self):
    print 'Selenium deleted.';

  def __str__(self):
    return 'This is Selenium.';

  def getName(self):
    ''' Class [ SeleniumKlass ] - getName(none) => Get self.name '''
    return self.name;

  def getUrl(self):
    ''' Class [ SeleniumKlass ] - getUrl(none) => Get self.url '''
    return self.url;

  def getDriver(self):
    ''' Class [ SeleniumKlass ] - getDriver(none) => Get self.driver '''
    return self.driver;

  def getWaiting(self):
    ''' Class [ SeleniumKlass ] - getWaiting(none) => Get self.waiting '''
    return self.waiting;

  def getScreenShot(self, imgPath):
    ''' Class [ SeleniumKlass ] - getScreenShot(imgPathStr) => Get Screenshot '''
    self.driver.save_screenshot(imgPath);

  def setFullScreen(self):
    ''' Class [ SeleniumKlass ] - setFullScreen(none) => Full Screen '''
    self.driver.maximize_window();

  def bind(self):
    ''' Class [ SeleniumKlass ] - bind(none) => Access [ Override ] '''
    driver = self.getDriver();
    driver.get(self.url);