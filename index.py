# -*- coding: utf-8 -*-

# Import
import common
common.init(['/klass'])

if __name__ == '__main__':

  # [Test] - Temlate Klass
  from Template import TemplateKlass
  x = TemplateKlass()
  x.setName('X')
  print x.getName()