class error_check:
    def __init__(self, data) -> None:
        self.data = data
        self.error = False
        self.output = 0
        self.checker()

    def checker(self):
        length = len(self.data)
        first = self.data[0: int(length/3) ]
        self.output = first
        second = self.data[int(length/3) : int((length/3)*2)]
        third = self.data[int((length/3) * 2): length]

        for i in range(0, len(first)):
            if not first[i] == second[i] or not second[i] == third[i]:
                self.error = True
                self.output[i] == int(int(( first[i] + second[i] + third[i] )) / 3)

test1 = error_check('100111001011001110010110011100101')
print(test1.error)
print(test1.output)

test2 = error_check('011101111101110111110111001111')
print(test2.error)
print(test2.output)