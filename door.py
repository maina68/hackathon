print("Enter 'help' to see this programs commands.You can then enter any command")
command = ""
opened = False
while True:
    command = input("> ").lower()
    if command == "open":
        if opened:
            print("The door is already open")
        else:
            opened = True
            print("The door is now open")
    elif command == "close":
        if not opened:
            print("The door is already locked")
        else:
            opened = False
            print("The door is now locked")
    elif command == "help":
        print("""
open - To open the door.
close - To lock the door
quit - To quit
        """)
    elif command == "quit":
        break
    else:
        print("Input is invalid!")
