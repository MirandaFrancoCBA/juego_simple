import random

class Apple:
    randx = random.randint(100, 600)
    randy = random.randint(100, 600)

    def comerManzana(self, x1,y1,x2,y2,bsize):
        if (x1 < x2 + bsize and x1 + bsize > x2) and (y1 < y2 + bsize and y1 + bsize > y2):  
            return True  
        return False 
    
    def nuevaManzana(self):
        self.randx = random.randint(100, 600)
        self.randy = random.randint(100, 600)