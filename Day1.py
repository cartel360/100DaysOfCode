option = ""
started = False

while option != 'quit':
    option = input("> ").lower()
    if option == 'help':
        print("Start - Start the car \nStop - Stop The car \nQuit - Close the program")
    elif option == 'start':
        if started:
            print("Car already Started!!!")
        else:
            started = True
            print("Car Started...")
    elif option == 'stop':
        if not started:
            print("Car already stopped!!!")
        else:
            started = False
            print("Car Stopped...")
    elif option == 'quit':
        print("Thank You...")
    else:
        print("I can't Understand that...")
