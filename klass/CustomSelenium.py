# -*- coding: utf-8 -*-
''' @ /klass/CustomSelenium.py '''

# Import
from _Selenium import SeleniumKlass

class CustomSeleniumKlass(SeleniumKlass):
  ''' Class [ CustomSeleniumKlass ] '''

  def __del__(self):
    print 'CustomSelenium deleted.'

  def bind(self):
    ''' Class [ CustomSeleniumKlass ] - bind(none) => Access '''
    driver = self.getDriver()
    driver.get(self.url)
    self.getScreenShot('./tmp/google.png')
    driver.close()