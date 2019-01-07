import random
import variables
import system


class Group(object) : #Group object has  number of solution and all gentic steps is done here  
    members =[] #list of solutions
    

    def __init__(self) : #creat initial number of solutions 
        for i in range(0,variables.number_Systems,1) : 
            System = system.System()
            self.members.append(System)
        
        
    def update(self) : #The main function in the class "every thing is done here 
        self.arrange() #arrange solutions "lowest traveled distance in the first"
        self.get_Children() #Make cossOver step betwen the best half members an random member of the first half members "every one have a chance"
        self.Make_gentic_Mutation() #Makes three tybes of Mutation : "1-break one crossedOver line , 2-one random swaping , 3-break the longest line"
        
        
        
    def arrange(self) : 
        for i in range(1,len(self.members),1) :
            for j in range(i,0,-1):
                if self.members[j].Cost < self.members[j-1].Cost :
                    swaper = self.members[j]
                    self.members[j] = self.members[j-1]
                    self.members[j-1] = swaper
                else :
                    break

                
    
        
        
    def get_Children(self) :
        for i in range(0,int((len(self.members)-1)/2),1) :
            #child_Order = self.get_Child(self.members[i],self.members[i+1])
            child_Order = self.get_Child(self.members[i],self.members[int(random.random()*(len(self.members)/2))])
            self.members[-(i+1)].Order = list(child_Order)
            self.members[-(i+1)].get_Cost()
        
    def get_Child(self,father,mother) : #get one child of two parends with random gens range 
        #part1_start_Point = int(random.random()*(number_Elements/2))
        part1_start_Point = int(random.random()*variables.number_Elements)
        #part1_end_Point = part1_start_Point + int(number_Elements/2)
        part1_end_Point = part1_start_Point + int(random.random()*(variables.number_Elements-part1_start_Point))
        
        part1 = list(father.Order[part1_start_Point:part1_end_Point])
        child_Order = list(mother.Order)
        for City in part1 :
            child_Order.remove(City)
        return child_Order + part1

    
    def genetic_Mutation(self,element,number_Mutations) : #actualy we makes one kind of mutation to save genetic princibles 
        for i in range (0,number_Mutations,1) :
            precent = int(random.random()*1)
            
            if  precent == 0 :
                Mutation1 = int(random.random()*variables.number_Elements)
                element.swaper(Mutation1 , element.first_worst_city_Number)

                
                Mutation2 = int(random.random()*variables.number_Elements)
                element.swaper(Mutation2 , element.second_worst_city_Number)
                
            
            elif precent == 20 or 10  :
                Mutation1 = int(random.random()*variables.number_Elements)
                Mutation2 = int(random.random()*variables.number_Elements)
                element.swaper(Mutation1 , Mutation2)
                
            else :
                my_Order = list(element.Order)
                my_Order.append(my_Order[0])
                done = False
                
                for i in range(0,variables.number_Elements,1) :
                   
                    for j in range(i+2,variables.number_Elements-1,1) :
                        if variables.line_List[my_Order[i].Number][my_Order[i+1].Number].is_Cross(variables.line_List[my_Order[j].Number][my_Order[j+1].Number]) :
                          
                            Mutation = int(random.random()*(variables.number_Elements-j))+j
                            if variables.number_Elements == j :
                                Mutation = int(random.random()*(variables.number_Elements))
                            element.swaper(Mutation , j+1)
                            done = True
                            break
                    if done :
                        break
                    
                
                
                
            
    def Make_gentic_Mutation(self):
        variables.k = variables.k + 1 
        for i in range(1,int(variables.number_Elements/2),1) :
            if (int(random.random()*1) == 1 ) :
                x = int(variables.number_Elements*(variables.number_Elements/(variables.number_Elements+variables.k)))+1
                self.genetic_Mutation(self.members[i],x)
            
            
                

            
    def print_Costs(self) :
        for i in range(0,len(self.members),1) :
            print(self.members[i].Cost)
