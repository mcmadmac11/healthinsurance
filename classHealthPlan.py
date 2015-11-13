class HDHP:
    def __init__(self, num1, num2):
        self.deductible = num1
        self.stop_loss = num2
        
    def calc_stop_loss(self, cost_of_procedure):
        

        if cost_of_procedure <= self.deductible:
            print(cost_of_procedure)
        elif self.deductible + ((cost_of_procedure - self.deductible) * .20) >=self.stop_loss:
            print(stop_loss)
        else:
            print (self.deductible + ((cost_of_procedure - self.deductible) * .20)) 

        
        



       
wtf = HDHP(5000, 7500)
wtf.calc_stop_loss(10000)




        
        



