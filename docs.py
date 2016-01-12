# -*- coding: utf-8 -*-

# Import
import common
common.init(['/klass'])

if __name__ == '__main__':

  import Template
  import _Selenium
  import CustomSelenium

  # Docs - common.py
  print common.__doc__
  print '  ' + common.log.__doc__
  print '  ' + common.init.__doc__

  print '\n'

  # Docs - klass/Template.py
  print Template.__doc__
  print '  ' + Template.TemplateKlass.__doc__
  print '  ' + Template.TemplateKlass.getName.__doc__
  print '  ' + Template.TemplateKlass.setName.__doc__

  print '\n'

  # Docs - klass/_Selenium.py
  print _Selenium.__doc__
  print '  ' + _Selenium.SeleniumKlass.__doc__
  print '  ' + _Selenium.SeleniumKlass.getScreenShot.__doc__
  print '  ' + _Selenium.SeleniumKlass.getDriver.__doc__
  print '  ' + _Selenium.SeleniumKlass.bind.__doc__

  print '\n'

  # Docs - klass/CustomSelenium.py
  print CustomSelenium.__doc__
  print '  ' + CustomSelenium.CustomSeleniumKlass.__doc__
  print '  ' + CustomSelenium.CustomSeleniumKlass.bind.__doc__

  print '\n'