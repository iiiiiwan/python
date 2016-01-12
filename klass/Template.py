# -*- coding: utf-8 -*-

''' @ /klass/Template.py '''

class TemplateKlass:
  ''' Class [ TemplateKlass ] '''

  def __init__(self):
    self.name = ''

  def __del__(self):
    print 'TemplateKlass deleted.'

  def __str__(self):
    return 'This is TemplateKlass.'

  def getName(self):
    ''' Class [ TemplateKlass ] - getName => Get self.name '''
    return self.name

  def setName(self, name):
    ''' Class [ TemplateKlass ] - setName => Set self.name '''
    self.name = name