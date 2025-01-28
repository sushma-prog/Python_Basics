import random 

class coin:

    def __init__(self, rare=False, clean=True, heads=True, **kwargs):
     
        for key,value in kwargs.items():
            setattr(self,key,value)

        self.is_rare = rare
        self.is_clean = clean 
        self.heads = heads 

        if self.is_rare:
            self.value = self.original_value * 1.25 
        else:
            self.value = self.original_value

        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour
    
    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def __del__(self):
        print("coin spent!")

    def flip(self):
        heads_options =[True,False]
        choice = random.choice(heads_options)
        self.heads = choice 
    
    def __str__(self):
        if self.original_value >= 1:
            return "{} pound coin".format(int(self.original_value))
        else:
            return "{} pence coin".format(int(self.original_value * 100))#for coins like 2 pence whose value is 0.02 this will give it as 2(because of 0.02 * 100)
        #now we wont get output as <__main__.One_Pence object at 0x000001D2CCE48080> instead we will get o/p as 1 pence coin or 1 pound coin etc.
        
class One_Pound(coin):
    
    def __init__(self):

        data = {
            "original_value": 1.00,
            "clean_colour": "gold",
            "rusty_colour": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5
        }
        
        super().__init__(**data)
        
#now, all we need to do is copy and paste all this data of pound coin and change some data to make it specific for each coin.

#lets start with pence coin and copy and change data from one pound coin.
class One_Pence(coin):

    def __init__(self):
        
        data = {
            "original_value": 0.01,#this is same copy as pound coin
            "clean_colour": "bronze",#this is specific colour for the pence coin.
            "rusty_colour": "brownish",#this is specifit for pence coin
            "num_edges": 1,#same as pound coin
            "diameter": 20.3,#specific to pence coin
            "thickness": 1.52,#specifit to pence coin
            "mass": 3.56#specific to pence coin
        }
        
        super().__init__(**data)

#next coin is two pence coin 
class Two_Pence(coin):

    def __init__(self):

        data = {
            "original_value": 0.02,
            "clean_colour": "bronze",
            "rusty_colour": "brownish",
            "num_edges": 1,
            "diameter": 25.9,
            "thickness": 1.85,
            "mass": 7.12
        }
        super().__init__(**data)

#next is five pence coin
class Five_Pence(coin):

    def __init__(self):

        data = {
            "original_value": 0.05,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 1,
            "diameter": 18.0,
            "thickness": 1.77,
            "mass": 3.25
        }
        super().__init__(**data)

        #since silver coins dont rust, we will override the rust method and set clean_colour for both clean and rust methods.
    def rust(self):
        self.colour = self.clean_colour

    def clean(self):
        self.clean = self.clean_colour

        #when you have same function name but it has different forms, shapes or versions of itself that is called polymorphism in oop.
        #poly means multiple and morph means forms so when a method has multiple forms inside a class, that is polymorphism.
        #here these rust and clean methods have multiple forms inside a class so this is polymorphism. 
        #so the way we do it is we override the rust and clean class that is inside parent class.  

#next is ten pence coin that is another silver coin.
class Ten_Pence(coin):

    def __init__(self):

        data = {
            "original_value": 0.10,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 1,
            "diameter": 24.5,
            "thickness": 1.85,
            "mass": 6.50
        }
        super().__init__(**data)

    def rust(self):
        self.colour = self.clean_colour

    def clean(self):
        self.clean = self.clean_colour

#twenty pence coin
class Twenty_Pence(coin):

    def __init__(self):

        data = {
            "original_value": 0.20,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 7,
            "diameter": 21.4,
            "thickness": 1.7,
            "mass": 5.00
        }
        super().__init__(**data)

    def rust(self):
        self.colour = self.clean_colour

    def clean(self):
        self.clean = self.clean_colour

#fifty pence coin
class Fifty_Pence(coin):

    def __init__(self):

        data = {
            "original_value": 0.50,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 7,
            "diameter": 27.3,
            "thickness": 1.78,
            "mass": 8.00
        }
        super().__init__(**data)

    def rust(self):
        self.colour = self.clean_colour

    def clean(self):
        self.clean = self.clean_colour

#two pound coin
class Two_Pound(coin):

    def __init__(self):

        data = {
            "original_value": 2.00,
            "clean_colour": "gold & silver",
            "rusty_colour": "greenish",
            "num_edges": 1,
            "diameter": 28.4,
            "thickness": 2.50,
            "mass": 12.00
        }
        super().__init__(**data)

#list of coins that inludes every type of coin.
coins = [One_Pence(),Two_Pence(),Five_Pence(),Ten_Pence(),Twenty_Pence(),Fifty_Pence(),One_Pound(),Two_Pound()]

for coin in coins:
    arguments = [coin,coin.colour,coin.value,coin.diameter,coin.thickness,coin.num_edges,coin.mass]

    string = "{} - colour:{}, value:{}, diameter(mm):{}, thickness(mm):{}, number of edges:{}, mass(gm):{}".format(*arguments)
    #to set it up we used .format also instead of putting in a load of parameters like, coin, coin.colour, coin.value, coin.diameter and so on we just unpacked all those parameters from list calledd arguments.

    #now, lets print out the string
    print(string)# with all the values like colour, value, diameter we also used coin directly so it will print out <__main__.One_Pence object at 0x000001D2CCE48080> for this coin which we dont want.
    #so in order to avoid this, we will use another method at top in the coin class.
