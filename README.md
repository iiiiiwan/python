<br />
---
<br />

### Print - Output
```Python
  print 'HOGE'
  print 'HOGE'
  print 'HOGE'
    # => HOGE
    # => HOGE
    # => HOGE

  print 'HOGE',
  print 'HOGE',
  print 'HOGE'
    # => HOGE HOGE HOGE
```

<br />
---
<br />

### Interactive Input
```Python
  name = raw_input('Enter Name : ')
    # => Interactive Mode
  print name
    # => Input String
```

<br />
---
<br />

### Load (Configuration For 'import')
```Python
  import sys, os
  sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/hogehoge')
```

<br />
---
<br />

### Class

**１-１． Import + Instance - import**
```Python
  import Template
  x = Template.TemplateKlass()
```


**１-２． Import + Instance - from + import**
```Python
  from Template import TemplateKlass
  x = TemplateKlass()
```


**２． Default Module**
```Python
  print x
    => ___str___
```
```Python
  del x
    => ___del___
```

**３． Custom Module**
```Python
  x.setName('HOGEHOGE')
  print x.getName()
```

<br />
---
<br />

### Loop - Array + For - index / value
```Python
  sampleList = ['A', 'B', 'C'];
  for idx, val in enumerate(sampleList):
    print str(idx) + ' - ' + str(val)
      # =>
      #   0 - A
      #   1 - B
      #   2 - C
```

<br />
---
<br />

### Default Exception - try + except

```Python
  try:
    print 'HOGE' + 0
  except TypeError:
    print 'TypeError'
      # => 'TypeError'
```

<br />
---
<br />

### Custom Exception - raise + try + except

```Python
  try:
    raise Exception('X', 'Y', 'Z')
  except Exception as err:
    print type(err)
    print err.args
    print err
    x, y, z = err.args
    print 'err.x : ' + x
    print 'err.y : ' + y
    print 'err.z : ' + z
      # => err.x : X
      # => err.y : Y
      # => err.z : Z
```

<br />
---
<br />

### Decolater

```Python
  def customDecolater(func):
    def wrapper():
      print '--- Decolater [ Start ] ---'
      func()
      print '--- Decolater [ End ] ---'
    return wrapper

  @customDecolater
  def bindCustomDecolater():
    print '\n=== Decolater [ Main ] ===\n'

  bindCustomDecolater()
    # => '--- Decolater [ Start ] ---'
    # => ''
    # => '=== Decolater [ Main ] ==='
    # => ''
    # => '--- Decolater [ End ] ---'
```

<br />
---
<br />

### Generator + Iterator
```Python
  # Generator
  def customGenerator():
    print '--- Not yielded ---'

    yield 'A'
    print '--- yielded [A] ---'

    yield 'B'
    print '--- yielded [B] ---'

    yield 'C'
    print '--- yielded [C] ---'

    yield 1
    print '--- yielded [1] ---'

    yield 2
    print '--- yielded [2] ---'

    yield 3
    print '--- yielded [3] ---'

  errCnt = 1
  tmpStack = ''
  gen = customGenerator()
  print '\n--- start ---\n'

  # Iterator
  try:
    print gen.next()
    print gen.next()
    print gen.next()
    print gen.next()
    print gen.next()
    print gen.next()
    print gen.next()
    print gen.next()
    print gen.next()
    print gen.next()
  except StopIteration:
    print '\n\tCatch [ StopIteration ] Error - ' + str(errCnt)
    errCnt += 1

  # =>
  #   --- start ---
  #   --- Not yielded ---
  #   A
  #   --- yielded [A] ---
  #   B
  #   --- yielded [B] ---
  #   C
  #   --- yielded [C] ---
  #   1
  #   --- yielded [1] ---
  #   2
  #   --- yielded [2] ---
  #   3
  #   --- yielded [3] ---
  #      Catch [ StopIteration ] Error - 1

```

<br />
---
<br />

### Delay - time + threading
```Python
  import time
  import threading

  def hogehoge():
    print 'XXX'

  t = threading.Timer(5, hogehoge)
  t.start()
    # => XXX after Thread's delayed 5s

  # time.sleep(2)
  # t.cancel()

    # => Cancel Thead's delay
```

<br />
---
<br />

### Directory List
```Python
  import glob
  ioDir = glob.glob('./tmp/*')
  print ioDir
    # => List up All File Name under [./tmp/]
```

<br />
---
<br />

### Read File - .txt
```Python
  f = open('./tmp/plainText.txt', 'r')
  for line in f:
    print line
      # => Each Line
```

<br />
---
<br />

### Read File - .json
```Python
  import json
  f = open('./tmp/sample.json', 'r')
  jsonData = json.load(f)
  print jsonData['GROUP_1']['a']
    # => 100
  print jsonData['GROUP_1']['A']
    # => KeyError

  print json.dumps(
    jsonData,
    sort_keys = True,
    indent = 2
  )
    # => Format Json
```

<br />
---
<br />

### Write File - Add - .txt
```Python
  str = '\nHOGEHOGEHOGE'
  f = open('./tmp/plainText.txt', 'a')
  f.write(str)
  f.close()
    # => Write '\nHOGEHOGEHOGE'
```

<br />
---
<br />

### Write File - New - .txt
```Python
  str = '\nHOGEHOGEHOGE'
  f = open('./tmp/plainText.txt', 'w')
  f.write(str)
  f.close()
    # => Create [./tmp/plainText.txt] + Write '\nHOGEHOGEHOGE'
```

<br />
---
<br />

### Write File - .json
```Python
  import json
  f = open('./tmp/sample.json', 'r')
  ff = json.dumps(
    json.load(f),
    sort_keys = True,
    indent = 2
  )
  f = open('./tmp/sample_ff.json', 'w')
  f.write(ff)
  f.close()
```

<br />
---
<br />

### Method

１． str - Number => String
```Python
  print 'Year' + 2016
    # => TypeError

  print 'Year' + str(2016)
    # => Year2016
```

<br />

２．random - **import random**
```Python
  print random.random()
    # => float (0.0 - 1.0)

  print random.uniform(1, 100)
    # => float (x - y)

  print random.randint(1, 100)
    # => int (x - y)

  print random.choice('abc')
    # => pickup

  sampleList = ['A', 'B', 'C']
  random.shuffle(sampleList)
  print sampleList
    # => shuffled array
```

<br />
---
<br />

### Lamda
```Python
  xxx = lambda num_1, num_2 : num_1 + num_2
    # => lambda x : y
    #      x == arguments
    #      y == return
  print xxx(1, 9)
    # => 10

  print (lambda num_1, num_2 : num_1 + num_2)(1, 9)
    # => 10
```

<br />
---
<br />

### Notice

１． No Increment(++) or Decrement(--)
```Python
  errCnt = 1
  errCnt++
  print errCnt
    # => SyntaxError

  errCnt = 1
  errCnt += 1
  print errCnt
    # => 2
```

<br />
---
<br />