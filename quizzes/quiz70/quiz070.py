import math
ips = []

def ipv4Machine():
    for i in range(1, 255**4+1):
        a = math.floor(i / 255 / 255 / 255 % 255)
        b = math.floor(i / 255 / 255 % 255)
        c = math.floor(i / 255 % 255)
        d = math.floor(i % 255)
        ips.append(f"{a}:{b}:{c}:{d}")

ipv4Machine()
print(ips)

def ipvyMachineV2():
    for a in range(1,255):
        for b in range(1,255):
            for c in range(1,255):
                for d in range(1,255):
                    ips.append(f"{a}:{b}:{c}:{d}")

