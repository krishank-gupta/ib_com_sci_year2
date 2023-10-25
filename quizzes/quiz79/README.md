# Quiz 079

## Handwritten Code

![handwritten code](/quizzes/quiz79/handwritten.png)

## Code

```.py
class palindrome:
    def __init__(self, inpA, inpB):
        self.inpA = inpA
        self.inpB = inpB
        self.outputs = []
        self.palindrome()

    def palindrome(self):
        for num in range(self.inpA, self.inpB+1):
            if self.reverse(num) == str(num):
                self.outputs.append(num)

    def reverse(self, num):
        out = []
        num = str(num)
        for i in range(len(num)-1, -1, -1):
            out.append(num[i])
        return ''.join(out)
    

test1 = palindrome(1,9)
test2 = palindrome(10,99)

print(test1.outputs)
print(test2.outputs)
```

## Proof

![proof](/quizzes/quiz79/proof.png)