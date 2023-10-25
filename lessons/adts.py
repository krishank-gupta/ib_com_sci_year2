class collection:
    def __init__(self):
        self.data = []
        self.location = 0

    def addItem(self, item):
        self.data.append(item)

    def isEmpty(self)->bool:
        return len(self.data)==0
    
    def hasNext(self)->bool:
        return self.location <= len(self.data)-1
    
    def getNext(self):
        if self.hasNext():
            item = self.data[self.location]
            self.location += 1
        else:
            item = f"[INDEX ERROR]. Collection out of index."
        return item
    
    def resetNext(self):
        self.location = 0

    def removeNext(self):
        self.data = self.data.pop(self.location)

x = collection()
# print(x.isEmpty())
x.addItem('bob')
# print(x.isEmpty())
# print(x.getNext())
# print(x.getNext())


# Cool methods to add
# add first
# remove next
# remove last
# sum integers
# additems

########################################################################################################################
# QUEUES
########################################################################################################################

# FIFO First In First Out

# methods
# enqueue()
# dequeue()
# isEmpty()

class queue:
    def __init__(self) -> None:
        self.data = []

    def enqueue(self, item):
        # item will be placed at the end
        self.data.append(item)

    def dequeue(self):
        # Returns the first element and removes from the queue
        item = self.data[0]
        self.data = self.data[1:]
        return item
    
    def isEmpty(self):
        return len(self.data) == 0

    def __repr__(self) -> str:
        return f" <Queue> {self.data} "
    
test = queue()

# test.enqueue('first')
# test.enqueue('second')
# test.enqueue('third')
# print(test.data)
# test.dequeue()
# print(test.data)


########################################################################################################################
# Stacks
########################################################################################################################

# LIFO Last In First Out

# methods
# pop()
# push()
# isEmpty()

class stack:
    def __init__(self):
        self.data = []

    def push(self, elem):
        self.data.append(elem)

    def pop(self):
        temp = []
        for i in range(len(self.data)-1):
            temp.append(self.data[i])

        self.data = temp

    def isEmpty(self):
        return len(self.data) == 0

    def __repr__(self) -> str:
        return f" <Stack> {self.data} "
    

test = stack()
test.push(1)
test.push(2)
test.push(3)
print(test.data)
test.pop()
print(test.data)
print(test.isEmpty())
