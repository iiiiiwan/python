# -*- coding: utf-8 -*-

# Import
import common
common.init(['/klass'])

if __name__ == '__main__':

  import Template

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