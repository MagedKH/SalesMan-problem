
import math

class Line(object) : #line object is a connection between two cities , with it we can test if there are a crossOver with another two cities connected with a line 
    #line equation : Y = mX + c
    X = [0,0]
    Y = [0,0]
    m = 0 
    c = 0
    
    def __init__(self,X,Y) :
        
        self.X = X 
        self.Y = Y

        if self.X[0] == self.X[1] : 
            self.m = math.inf 
        else :
            self.m = (self.Y[1]-self.Y[0])/(self.X[1]-self.X[0])
        self.c = (self.Y[0])-(self.m*self.X[0])
        
    def is_Cross(self,my_Line) : #test if there are any CrossOver with another line 
        my_point_C = (self.c-my_Line.c)
        my_point_M = (my_Line.m-self.m) 
        
        if my_Line.m == self.m :
            return False
        else :
            my_Xpoint = my_point_C/my_point_M
            if ((my_Xpoint < self.X[0]) and (my_Xpoint > self.X[1])) or ((my_Xpoint < self.X[1]) and (my_Xpoint > self.X[0])) :
                return True 
            else :
                return False
