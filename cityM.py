import math
import variables

class City(object) : #the smalest object in the code 
    X = 0
    Y = 0
    Number = 0
    Name = ""
        
    def __init__ (self,city_Number) :
        self.Number = city_Number
        self.X    = int(variables.data[0+city_Number*3])
        self.Y    = int(variables.data[1+city_Number*3])
        self.Name = variables.data[2+city_Number*3]
        
    def calculat_Cost(self,destination_City) : #Calculate distance between "Me" and the directed City   
        return int(math.sqrt(pow((self.X-destination_City.X),2)+pow((self.Y-destination_City.Y),2)))
