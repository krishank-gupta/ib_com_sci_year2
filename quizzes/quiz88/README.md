# Quiz 88

## Code

```.py
def SUMR(x):
    if not x:
        return 0
    else:
        return x[0] + SUMR(x[1:])
```
