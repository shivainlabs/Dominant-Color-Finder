`palette_size=(w,h)` Create a small image that is `w` pixels wide and `h` pixels tall.

![Draw Rectange](/images/image-4.png)

`draw.rectangle()` tells PIL : Draw a rectange between these two points.
    `[x1, y1, x2, y2]`

## 1. Our co-ordinate system is like this : 
![Coordinate](/images/image-5.png)

Our co-ordinates : 
```
[0, 0, 60, 50]
[60, 0, 120, 50]
[120, 0, 180, 50]
```
<br></br>

## 2. For first co-ordinate 

![First-Co-ordinate](/images/image-6.png)


## 3. Hexadecimal Formatting 

![Hexadecimal Formatting](/images/image-7.png)
<br>

![Formatting Example](/images/image-8.png)

<br>

## 4. In brightness how do we find the brightnees?

![brightness formula](/images/image-9.png)

So when green changes by 100 units, it has a much larger effect on the calculated luminance than blue changing by 100 units.

## 5. Text Color

![Text Color](/images/image-10.png)

`text_color = "black" if brightness > 128 else "white"`