import shared

number_Elements = shared.number_Elements
time = 3 #the time to find solution 
number_Systems  = int(4*number_Elements) # found this equation by tries "giving better solutions 
number_Groups   = 1 
k = 1
global best_Order #final solution "the communication with GUI"

cost_List       = [[i * j for j in range(number_Elements)] for i in range(number_Elements)] #empty two dimention list with dimention (number_Elements*number_Elements)
line_List       = [[i * j for j in range(number_Elements)] for i in range(number_Elements)]
first_System    = []
arranged_cost_List = []

data = []



for cities in range(0 , number_Elements , 1) :#getting cities information from GUI 
        data.append( shared.generated_nodes[cities].x)
        data.append( shared.generated_nodes[cities].y)
        data.append( shared.generated_nodes[cities].index)