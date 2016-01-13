# -*- coding: utf-8 -*-

# Import
import common
common.init(
  [
    '/klass',
    '/klass/implements'
  ]
)

# Sub Import
from GoogleSelenium import GoogleSeleniumKlass

if __name__ == '__main__':

  # [Test] - GoogleSelenium Klass
  test = GoogleSeleniumKlass(
    'Google',
    'https://www.google.co.jp/'
  );
  test.bind();