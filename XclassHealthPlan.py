class HDHP:
    def __init__(self):
        self.deductible = '500'
        self.stop_loss = 7500
        self.monthly_prem = 500
        self.name = "Arise"
        
    def deductible(self):
        self.deductible = 5000
        print("The annual deductible for the plan you have chosen is $5000")
        return self.deductible
        
    def stop_loss(self):
        self.stop_loss = 7500
        print("Your maximum out of pocket costs for this plan are $7500 ")
        return self.stop_loss
    def monthly_prem(self):
        self.monthly_prem = 500
        return self.monthly_prem
    def plan_name(self):
        self.plan_name = 'Arise'
        print("The Insurance Plan you've selected is: Arise Health Plan")

        
        
