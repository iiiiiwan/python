<br />
---
<br />

### Ref

[Ref - 1 = Install NumPy + OpenCV](http://opencv.blog.jp/python/%E4%BD%BF%E3%81%84%E6%96%B9)

<br />
---
<br />

### Module
```Python
  import numpy as np
  import cv2
```

<br />
---
<br />

### Load Image
```Python
  img = cv2.imread(
    './tmp/sample.png',
    cv2.IMREAD_UNCHANGED
  );

  # cv2.imread('Image Path', Load Mode)
  # Load Mode
  #   cv2.IMREAD_COLOR [default] => Full Color Withiout Transparency
  #   cv2.IMREAD_GRAYSCALE       => Black and White
  #   cv2.IMREAD_UNCHANGED       => Full Color With Alpha
```

<br />
---
<br />

### Display Image
```Python
  cv2.imshow('Sample Image', img);
    # => cv2.imshow('Window Name', cv2.imread)
  cv2.waitKey(0);
    # => Wait Key Input
  cv2.destroyAllWindows();
    # => Close All Window
```