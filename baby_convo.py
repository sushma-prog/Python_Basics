from random import choice#importing random function

baby_questions = ["why is the sky blue?: ","why is there a face on the moon?: ","where are all the dinosaurs?: "]

question = choice(baby_questions)
answer =input(question).strip().lower()

while answer != "just because":
    answer = input("why?: ").strip().lower()#lower because we want answer as just because! which is in lowercase

print("Oh...Okay!")    
