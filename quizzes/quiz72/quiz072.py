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

test1 = macGenerator(10)
print("Random")
print(test1.output)

test2 = macGeneratorWithMaker(5, "ab:cd:ef")
print("Known Maker (ab:cd:ef):")
print(test2.output)