import random #to flip coin randomly, we need to call a library called random.

class pound: 
    
    def __init__(self, rare=False): #this __init__ method is constructor

        self.rare = rare

        if self.rare: 
            self.value = 1.25
        else:
            self.value = 1.00
        
        self.colour = "gold"
        self.num_edges = 1
        self.diameter = 22.5 #mm
        self.thickness = 3.15 #mm
        self.heads = True

    def __del__(self):#this __del__ method is our destructor. it can be written anywhere it doesnt need to be at the bottom.
        print("coin spent!")#this will print coin spent when the coin has been destroyed.

    #to create a method, we need to be inside of class.

    def rust(self):#the first parameter to any class method has to be self or more correctly, whatever you wrote inside() of, def __init__()
        self.colour = "greenish"

    #lets create a new method called clean to clean the rusted coins.
    def clean(self):
        self.colour = "gold"

    #lets create a method to flip the coin randomly.
    def flip(self):
        heads_options =[True,False]#list from which, random will select random value. as we set state of head as True so now, this list will be for if heads is True or False.
        choice = random.choice(heads_options)# the random choice selected by random.choice will be stored in choice variable.
        self.heads = choice #now, it will be selected randomly if it is heads for a coin or not.

coin1 = pound()#we created an coin1 object.
del coin1#this will spen the coin
#coin1# as now coin1 is distroyed, calling coin1 would show an error of, name 'coin1' is not defined.
    
