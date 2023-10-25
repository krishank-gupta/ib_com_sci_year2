# Quiz 072

## Handwritten Code

![handwritten code](/quizzes/quiz72/handwritten.png)

## Code

```.py
from random import randint

class macAddressGenerator:
    def __init__(self, amount) -> None:
        self.chars = '0123456789ABCDEF'
        self.adr = ''
        self.amount = amount
        self.generator()

    def charGenerator(self):
        rand = randint(0,15)
        char = self.chars[rand]
        return char
    

    def pairGenerator(self):
        self.adr += self.charGenerator()
        self.adr += self.charGenerator()
        self.adr += ":"

    def generator(self):
        for i in range(0,self.amount):
            self.pairGenerator()
        self.adr = self.adr[:-1]

class macGenerator:
    def __init__(self,N):
        self.N = N
        self.output = []
        self.run()

    def run(self):
        for i in range(self.N):
            out = macAddressGenerator(6)
            self.output.append(out.adr)

test1 = macGenerator(4)
print(test1.output)

```

The above code generates random mac addresses. If the maker of the mac address is known and the first 3 pairs are known, the code can be modified to generate mac addresses specific to the maker. Here is the updated code:

```.py
class macGeneratorWithMaker:
    def __init__(self,N, maker):
        self.N = N
        self.maker = maker
        self.output = []
        self.run()

    def run(self):
        for i in range(self.N):
            out = macAddressGenerator(3)
            output = self.maker + ":" + out.adr
            self.output.append(output)

test2 = macGeneratorWithMaker(5, "aa:aa:aa")
print(test2.output)
```

## Proof

![proof](/quizzes/quiz72/proof.png)