Known_users = ["Alice","Bob","Claire","Emma","Fred"<"Georgie","Harry"]

while True:
    print("Hi! my name is Travis")
    Name=(input("enter your name: ")).strip().capitalize()

    if Name in Known_users:
        print("Hello {}!".format(Name)) # or print("hello",Name,"!")
        Remove = input("would you like to be removed from the system (y/n)?: ").strip().lower()

        if Remove == "y":
            Known_users.remove(Name)
        elif Remove == "n":
            print("No problem, I didn't want you to leave anyway!")   

    else:
        print("hmmm I don't think I have met you yet {}".format(Name))  
        add_me = input("would you like to be added to the system (y/n)?: ").strip().lower()

        if add_me == "y":
            Known_users.append(Name)#will add Name at end of the list.
        elif add_me == "n":
            print("No worries, see you around!")   
