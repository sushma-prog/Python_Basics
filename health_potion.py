import random

health = 50

difficulty = random.randint(1,3)
print("difficulty =",difficulty)

health_potion = int(random.randint(25,50)/difficulty)

health = health + health_potion

print("health =",health)


#When you write import random in Python, it means you want to use a set of tools that can help you do things randomly in your program.
#It's like having a dice or a coin to make decisions or generate numbers without any specific pattern.
#For example, you can use random.randint(a, b) to generate a random integer between a and b.
#The random module provides functions to make your program more unpredictable and dynamic.
