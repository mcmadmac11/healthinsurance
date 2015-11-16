class Health_plan:

   
    def __init__(self, num1, num2, percent):
        self.deductible = num1
        self.stop_loss = num2
        self.splitcost = percent

        
    def calc_stop_loss(self, cost_of_procedure):
        if cost_of_procedure <= self.deductible:
            print("Your bill for this plan would be: $",cost_of_procedure)
        elif self.deductible + ((cost_of_procedure - self.deductible) * self.splitcost) >= self.stop_loss:
            print("Your bill for this plan would be: $", self.stop_loss)
        else:
            print("Your bill for this plan would be:$", self.deductible + ((cost_of_procedure - self.deductible) * self.splitcost))
    


        


       
plan1 = Health_plan(4000, 8000, .10)
plan1.calc_stop_loss(10000)
plan2 = Health_plan(3000, 12000, .30)
plan2.calc_stop_loss(10000)
