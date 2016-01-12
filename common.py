# -*- coding: utf-8 -*-

''' @common.py '''

# Import
import sys
import os
import datetime

# For Log
def log(title, msg):
  ''' common - [log(titleStr, msgStr) => Output Log.] '''
  print '\n'
  print '======= [ ' + title + ' ] ======='
  print msg
  print '\n'

# For Current Time
def getCurrentTime():
  ''' common - [getCurrentTime(none) => Get Current Time.] '''
  d = datetime.datetime.today()
  return (d.year, d.month, d.day, d.hour, d.minute, d.second, d.microsecond)

# For Init
def init(dir):
  ''' common - [init(dirArr) => Bind Module Directory.] '''
  for tmpDir in dir:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + tmpDir)
  log('common.py', 'Configuration Done.')