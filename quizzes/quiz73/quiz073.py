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

class routing_table:
    def __init__(self) -> None:
        self.routing_table = {}

    def validation(self, mac_adr):
        if (mac_adr.count(':') == 5 and len(mac_adr) == 17):
            return mac_adr
    
    def processor(self, input):
        self.input = self.validation(input)

        if self.input in self.routing_table.keys():
            print(self.input, self.routing_table[self.input])
        
        else:
            self.routing_table[self.input] = IPV6Machine(1).output
            print(self.routing_table)

test1 = routing_table()
test1.processor('00:1A:2B:3C:4D:5E')
test1.processor('12:34:56:78:90:AB')
test1.processor('00:1A:2B:3C:4D:5E')
test1.processor('FF:EE:DD:CC:BB:AA')
