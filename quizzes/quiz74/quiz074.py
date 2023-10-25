class build_data_pkg:
    def __init__(self,Mac_rx, IP_rx, Mac_sx, IP_sx, data):
        self.Mac_rx = str(Mac_rx)
        self.IP_rx = IP_rx
        self.Mac_sx = Mac_sx
        self.IP_sx = IP_sx
        self.data = data
        self.output = []
        self.load()

    def load(self):
        for i in range(0, int(len(self.data)/4)+1):
            load_data = self.data[4*i : (i+1)*4]
            index = i
            self.msg(load_data, index)

    def msg(self, load_data, index):
        out = f"{self.Mac_rx} | {self.IP_rx} | {self.Mac_sx} | {self.IP_sx} | {index} | {load_data}"
        self.output.append(out)


test1 = build_data_pkg("80:90:AA:F0:22:11", "192.168.1.2", "30:AA:1A:F1:00:AE", "192.168.1.3", "Hello world")

print(test1.output)
