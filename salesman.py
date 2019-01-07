#Solvin SalesMan problem using Simulated Annealing algorithm 
#This Code is done using java
#so we saves cities information in a file
#then we makes a process to run java code which saves solution in another file
#after that we takes solution from the file and send it to GUI 

#files related to this code : SalesMan.jar 
#Folder related to this code : SalesMan  "not used in running algorithm just for more information"
#Done by: Asmaa Abd El_Naser

import subprocess
import shared

best_Order = [] #shared final solution with GUI
information_file_Name = "informationFile.txt" # where java code saves solution 

def main_Loop():
    creat_Data () #save cities information "X,Y,Name" in file 
    global best_Order 
    subprocess.call(['java', '-jar', 'SalesMan.jar']) # direction of the java code which a '.jar' file
    file = open(information_file_Name) 
    best_Order = file.readlines()
    file.close()
    #print (best_Order)
    
def creat_Data () :
    dataFile = "dataFile.txt" # where java code takes information of cities to work on  
    data = []
    file = open(dataFile,'w')    
    for cities in range(0 , shared.number_Elements , 1) :
        data.append( str(shared.generated_nodes[cities].x)+"\r")
        data.append( str(shared.generated_nodes[cities].y)+"\r")
        data.append( str(cities)+"\r")
            
    file.writelines(data)
    file.close()



#main_Loop()