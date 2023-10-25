class converter:
    def __init__(self, inp) -> None:
        self.inp = inp
        self.output = []
        self.words()

    def binary(self, char):
        num = ord(char)
        out = ""
        while num != 0:
            out = f"{num % 2}" + out
            num = num // 2
        if len(out) != 8:
            out = "0"*(8-len(out))+out
        
        return out

    def words(self):
        for i in self.inp:
            self.output.append(self.binary(i))

        self.output = ' '.join(self.output)

test1 = converter('Hello World!')
print(test1.output)

test2 = converter('42 is the answer.')
print(test2.output)

test3 = converter('ABC123')
print(test3.output)