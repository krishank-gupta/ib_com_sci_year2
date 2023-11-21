# Quiz 86

## Python Code

```.py
class CalorieCount:
    def __init__(self,daily_limit) -> None:
        self.daily_limit = daily_limit
        self.daily_intake = 0
        self.protein = 0
        self.carbs = 0
        self.fat = 0

    def addMeal(self,daily_intake,pro,carb,fat):
        self.daily_intake+=daily_intake
        self.protein+=pro
        self.carbs+=carb
        self.fat+=fat

    def getProteinPercentage(self):
        return round(4*self.protein /self.daily_intake,2)
    
    def onTrack(self):
        if self.daily_intake < self.daily_limit:
            return True
        else:
            return False

sunday = CalorieCount(1500)

sunday.addMeal(716,38,38,45)
sunday.addMeal(230,16,8,16)
sunday.addMeal(568,38,50,24)

print(sunday.onTrack())
print(sunday.getProteinPercentage())
```

