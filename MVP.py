class HealthPlan:
    def __init__(self, num1, num2, percent):
        self.deductible = num1
        self.stop_loss = num2
        self.splitcost = percent
        
    def calc_stop_loss(self, cost_of_procedure):
        if cost_of_procedure <= self.deductible:
            print("Your bill for the procedure is: $",cost_of_procedure)
        elif self.deductible + ((cost_of_procedure - self.deductible) * self.splitcost) >=self.stop_loss:
            print("Your bill for the procedure is: $",stop_loss)
        else:
            print("Your bill for the procedure is: $",self.deductible + ((cost_of_procedure - self.deductible) * self.splitcost))
            

        
        


        
compute = HealthPlan(5000, 7500, .10)
compute.calc_stop_loss(10000)




        