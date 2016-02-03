# -*- coding: utf-8 -*-
''' @ /klass/GoogleSelenium.py '''

# Import
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

# Sub Import
from _Selenium import SeleniumKlass

class GoogleSeleniumKlass(SeleniumKlass):
  ''' Class [ GoogleSeleniumKlass ] '''

  def __del__(self):
    print 'GoogleSelenium [ ' + self.getName() + ' ] deleted.';

  def bind(self):
    ''' Class [ GoogleSeleniumKlass ] - bind(none) => Access '''
    driver = self.getDriver();
    try:
      driver.get(self.url);
      elem = driver.find_element(
        By.XPATH,
        '//*[@id="lst-ib"]'
      );
      elem.send_keys('python');
      elem.send_keys(self.keys.RETURN);
      self.getWaiting().until(EC.title_contains('- Google'));
    except NoSuchElementException:
      print '\n-+-+-+- NoSuchElementException -+-+-+-\n';
    except TimeoutException:
      print '\n-+-+-+- TimeoutException -+-+-+-\n';
    finally:
      print '\nFin.\n'
      driver.close();

# Sub Import
# from GoogleSelenium import GoogleSeleniumKlass;
## [Test] - GoogleSelenium Klass
# test = GoogleSeleniumKlass(
#   'Google',
#   'https://www.google.co.jp/'
# );
# test.bind();