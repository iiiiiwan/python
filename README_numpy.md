# Numpy

<br>

### １． numpy.array

  > Numpy用配列を生成

  1. 配列内要素の型は全て同じ
  2. 配列長は固定 (固定長配列)
  3. 配列の各次元の要素数は同じ

```Python
  test = np.array(
    [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]
  );
```

<br />
---
<br />


#### ２． Numpy型配列の情報取得

  **Numpy型配列.flags**

  > メモリ上の詳細情報

```Python
    print test.flags
      # =>
      #    C_CONTIGUOUS : True
      #    F_CONTIGUOUS : False
      #    OWNDATA : True
      #    WRITEABLE : True
      #    ALIGNED : True
      #    UPDATEIFCOPY : False
```

<br>

  **Numpy型配列.ndim**

  > 次元数

```Python
    print test.ndim
      # => 2
```

<br>

  **Numpy型配列.size**

  > 総要素数

```Python
    print test.size
      # => 9
```

<br>

  **Numpy型配列.shape**

  > 各次元の要素数 - (縦, 横)

```Python
    print test.shape
      # => (3L, 3L)
```

<br>

  **Numpy型配列.itemsize**

  > 1要素のバイト数

```Python
    print test.itemsize
      # => 4
```