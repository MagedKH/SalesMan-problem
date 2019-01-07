import random
import math
import variables

class System(object) : #The solution of number of cities "have the Order of cities, the Order's cost, the worst gen (first and second worst city) which has the longest distance
    
    Order = list(variables.first_System)
    Cost = math.inf     
    first_worst_city_Number  = 0      
    second_worst_city_Number = 0  
    worst_Cost = math.inf
    
    def __init__(self): #get random Order with its cost
        self.Order = self.random_Order(list(variables.first_System))
        self.get_Cost()

    def get_Cost(self) : #calculate the new order or mutated order's cost
        my_List = list(self.Order)
        my_List.append(my_List[0]) #salesMan must return to his home after he finishes work 
        
        self.first_worst_city_Number = 0
        self.second_worst_city_Number = 0
        self.worst_Cost = math.inf
        self.Cost = self.calculat_system_Cost(my_List)
        

    def calculat_system_Cost(self,my_List) : #Calculates the Order cost and find the worst gen 
        
        if len(my_List) == 1 :
            return 0
        else :            
            current_City = my_List.pop(0)
            initial_Cost = variables.cost_List[current_City.Number][my_List[0].Number]
            if initial_Cost < self.worst_Cost :
                self.worst_Cost = initial_Cost 
                self.second_worst_city_Number = len(self.Order) - len(my_List)
                self.first_worst_city_Number = self.first_worst_city_Number - 1
            return  initial_Cost + self.calculat_system_Cost(list(my_List))
        
    def swaper(self,City1,City2) : #swaping between two cities in my Order
        swaper = self.Order[City1]    
        self.Order[City1] = self.Order[City2]
        self.Order[City2] = swaper
        self.get_Cost()
        
    def translate_Order(self): #takes the Order of my system which [have Order of object cities] and return a list of ordered cities Number
        my_List = []
        for element in self.Order :
            my_List.append(element.Number) #using Number not Name becouse of some "communication with GUI" issues 
        #my_List.append(self.Order[0].Name)
        my_List.append(self.Cost)
        return my_List
        
    def random_Order(self,my_List): #makes a random order of citie then takes the first city and choice the second city randomly with the first half closest cities and so on
        new_List = []
        for i in range (0,variables.number_Elements,1) : #makes random Order
            new_List.append(my_List.pop(int(random.random()*(variables.number_Elements-i))))  
        #return new_List
        #precent = random.random()*(1-(1.6/(variables.number_Elements+1)))
        precent = random.random()
        Order = []  
        current_City = new_List[0]
        Order.append(current_City)
        new_List.remove(current_City)
        k = 0
        
        while len(new_List) > 0 :
            if k == 2 : #can't find solution with the current precentage so make a new one 
                precent = random.random() 
                #precent = random.random()*(1-(1.6/(variables.number_Elements+1)))
                k = 0 
                
            for i in range(0,int(variables.number_Elements),1) :
                #if ((variables.first_System[variables.arranged_cost_List[current_City.Number][i]] not in Order) and (precent <(1-(1.6/(i+1))))) :
                if ((variables.first_System[variables.arranged_cost_List[current_City.Number][i]] not in Order) and (precent < (i/(variables.number_Elements/2)))) : #the sequance (i/(variables.number_Elements/2)) makes better chance for closest cities  
                    Order.append(variables.first_System[variables.arranged_cost_List[current_City.Number][i]])
                    current_City = Order[-1]
                    new_List.remove(current_City)
                    k = 0
                    break
            k = k + 1
        return Order
