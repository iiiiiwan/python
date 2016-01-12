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

### Method

１． str - Number => String
```Python
print 'Year' + 2016
  # => TypeError

print 'Year' + str(2016)
  # => Year2016
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