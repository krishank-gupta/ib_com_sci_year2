# Quiz 071

## Handwritten Code

![handwritten code](/quizzes/quiz71/handwritten.png)

## Code

```.py

from random import randint

class IPV6:
    def __init__(self) -> None:
        self.adr = ''
        self.chars = '1234567890ABCDEF'
        self.IPGENERATOR()

    def OCTETGENERATOR(self):
        octet = ''
        for i in range(0,4):
            rand = randint(0,15)
            octet += self.chars[rand]
        octet += ':'
        return octet
    
    def IPGENERATOR(self):
        for i in range (0,8):
            self.adr += self.OCTETGENERATOR()
        self.adr = self.adr[:-1]

class IPV6Machine:
    def __init__(self, N) -> None:
        self.N = N
        self.output = []
        self.generator()

    def generator(self):
        for i in range(0, self.N):
            ip = IPV6()
            self.output.append(ip.adr)

test1 = IPV6Machine(5)
print(test1.output)

test2 = IPV6Machine(3)
print(test2.output)
```

## Proof

![proof](/quizzes/quiz71/proof.png)
