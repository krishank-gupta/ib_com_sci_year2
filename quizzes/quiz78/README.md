# Quiz 078

## Handwritten Code

![handwritten code](/quizzes/quiz78/handwritten.png)

## Code

```.py
class layer4_firewall:
    def __init__(self,data):
        self.data = data[16: len(data)-1]
        self.error = ''
        self.output = ''
        self.bin = data[0:16]
        self.out()

    def toDecimal(self, bin):
        num = 0

        for i in range(15, 0, -1):
            if bin[i] == '1':
                num += (2 ** (15-i))

        return num
    
    def out(self):
        if self.toDecimal(self.bin) == 80 or self.toDecimal(self.bin) == 22123:
            self.error = 'Allowed'
            self.output = self.data

        else:
            self.error = 'filtered'
            self.output = None


test1 = layer4_firewall('100111001011001110010110011100101')
print(test1.error, test1.output)
test2 = layer4_firewall('010101100110101111110111001111')
print(test2.error, test2.output)
```

## Proof

![proof](/quizzes/quiz78/proof.png)