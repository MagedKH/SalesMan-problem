#Here the shared area between GUI and all Algorithms 

number_Elements = 0
generated_nodes = {}
initial_state = 0

algorithm1 = [] #soluthion of Gentic Algorithm "Cost is the last element"
algorithm2 = [] #solution of Simulated Annealing Algorithm "Cost is the last element"
algorithm3 = [] #solution of Tabu Algorithm "Cost is the last element"

def trans_result(result,state): #Makes the first city "in solution" salesMan's home which Inputted by user
    k = 0
    for elem in result :
        if int(elem) == state :
            break 
        k += 1
    
    my_List= []
    for i in range( k , len(result) , 1):
        my_List.append(int(result[i]))
 
    for i in range( 0 , k  , 1 ) :
        my_List.append(int(result[i]))
  
    return my_List
  
def algorithm1_result(): #Makes gentic solution Understandable to the GUI Code
    cost = algorithm1.pop(-1)
    List = trans_result(list(algorithm1) ,initial_state )
    List.append(List[0])
    List.append(cost)
    
    return List
    
def algorithm2_result(): #Makes Simulated Annealing solution Understandable to the GUI Code
    cost = algorithm2.pop(-1)
    List = trans_result(list(algorithm2) ,initial_state )
    List.append(List[0])
    List.append(cost)

    return List

def algorithm3_result(): #Makes Tabu solution Understandable to the GUI Code
    cost = algorithm3.pop(-1)
    List = trans_result(list(algorithm3) ,initial_state )
    List.append(List[0])
    List.append(cost)

    return List



