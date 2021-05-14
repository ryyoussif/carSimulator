car = "stopped" #car initially stopped
while True:
    command = input(">").lower()
    if command == "help":
        print('''start - to start the car
stop - to stop the car
quit - to exit''')
    elif command == "start":
        if car == "stopped":
            print("Car started...Ready to go!")
            car = "started"
        else:
            print("Car already started.")

    elif command == "stop":
        if car == "started":
            print("Car stopped.")
            car = "stopped"
        else:
            print("Car already stopped!")

    elif command == "quit":
        break
    else:
        print("I don't understand that")
