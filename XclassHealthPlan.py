class Policy:
    def __init__(self, num):
        self.deductible = num

    def get_deductible(self):
        self.deductible = 5000
        print("The annual deductible for the plan you have chosen is $5000")
        return self.deductible
        
dan = Policy(5000)
        
        
