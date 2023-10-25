# Quiz 077

## Handwritten Code

![handwritten code](/quizzes/quiz76/handwritten.png)

## Code

```.py
class parity_check:
    def __init__(self, data) -> None:
        self.data = data
        self.ones = 0
        self.output = False
        self.counter()

    def counter(self):
        for i in range(1, len(self.data)):
            if self.data[i] == '1':
                self.ones += 1

            if (self.data[0] == '1' and self.ones%2==0) or (self.data[0]=='0' and self.ones%2==1):
                self.output = False
            else:
                self.output = True

test1 = parity_check("100111001011001110010110011100101")
print(test1.output)

test2 = parity_check("011101111101110111110111001111")
print(test2.output)
```

## Proof

![proof](/quizzes/quiz77/proof.png)