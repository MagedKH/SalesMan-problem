#Solvin SalesMan problem using Gentic algorithm 
#files related to this code : variables.py ,cityM.py ,line.py ,system.py ,group.py
#Done by: Maged Khaled Ahmed

import datetime
import cityM
import line
import group
import variables
import shared



def main_Loop():
    
    #a = datetime.datetime.now()    
    creat_the_first_System() # creat array of city objects with index 0:nomber of nodes
    calculat_static_Costs() # calculate diastance between all nodes to reduce time cost 
    creat_update_Group()    # creat number of group objects each group has number of system object each system has order of city objects
    #print ("Time = \r", datetime.datetime.now() - a)
    

def creat_the_first_System():
    
    for cities in range(0 , variables.number_Elements , 1) :#getting cities information from GUI 
        variables.data.append( shared.generated_nodes[cities].x)
        variables.data.append( shared.generated_nodes[cities].y)
        variables.data.append( shared.generated_nodes[cities].index)
    
    for i in range(0,variables.number_Elements,1) :
        new_City = cityM.City(i)
        variables.first_System.append(new_City)
    
def calculat_static_Costs ():
   
    for i in range(0,variables.number_Elements,1) :
        for j in range(i,variables.number_Elements,1) :
            variables.cost_List[i][j] = variables.first_System[i].calculat_Cost(variables.first_System[j])
            variables.cost_List[j][i] = variables.cost_List[i][j]
            
            variables.line_List[i][j] = line.Line([variables.first_System[i].X , variables.first_System[j].X] , [variables.first_System[i].Y , variables.first_System[j].Y])
            variables.line_List[j][i] = variables.line_List[i][j]  
        
        variables.arranged_cost_List.append(i) 
        variables.arranged_cost_List[i] = arrange(list(variables.cost_List[i]))           
    
    
def arrange(my_List) : #helpfull function to make dectionery with key = number of city , value = array of costs between the key city and other cities , finally arrange this lists 
    my_Dictionery = {}
    for i in range(0,len(my_List),1) :
        my_Dictionery.update({i:my_List[i]})
    return sorted(my_Dictionery, key = my_Dictionery.__getitem__)
                        
def find_best_Member(my_List) : #test my solution to find the best member which excest in the first of each group list of members
    best_Group = my_List[0] 
    for Group in my_List :
        if Group.members[0].Cost < best_Group.members[0].Cost :
            best_Group = Group
    return best_Group
   
    
        
def creat_update_Group() : 
    list_Groups = []
    for i in range(0,variables.number_Groups,1) :
        a = datetime.datetime.now().hour*60*60+datetime.datetime.now().minute*60 
        a += datetime.datetime.now().second + ((datetime.datetime.now().microsecond)/1000000)
        list_Groups.append(group.Group())
        while True :
            b = datetime.datetime.now().hour*60*60+datetime.datetime.now().minute*60 
            b += datetime.datetime.now().second + ((datetime.datetime.now().microsecond)/1000000) - a
            list_Groups[i].update()
            if b > (variables.time/variables.number_Groups)  :
                break
            
    best_Group = find_best_Member(list_Groups)
    save_Data(best_Group.members[0])

def save_Data(best_Member) : # save my result in a shred array to make easy communication with GUI Code 
    variables.best_Order = best_Member.translate_Order()  
       
        
#main_Loop()
        

