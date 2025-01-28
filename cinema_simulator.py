films ={
    "Iron man 2":[3,5],
    "Barbie":[18,5],
    "Avengers:end game":[15,5],
    "Avatar 2":[12,5]
}

print('''
Films availabe:
    Iron man 2
    Barbie
    Avengers:end game
    Avatar 2
      ''')

while True:

    Choice = input("what movie would you like to watch?: ").strip().capitalize()

    if Choice in films:
        age = int(input("How old are you?: ").strip())
        
        if age >=films[Choice][0]:#here it will check film dictionary then choice that is movie then 0th index that is age
            
            num_seats = films[Choice][1]

            if num_seats > 0:#it will check if there are enough tickets in index 1
                print("Enjoy the film!")#if age is greater than  required age and tickets are avilable then give permission
                films[Choice][1] = films[Choice][1] - 1

            else:
                print("Sorry, we are sold out!")

        else:
                 print("You are too young to see that film!")

    else:
        print("we don't have that film...")
