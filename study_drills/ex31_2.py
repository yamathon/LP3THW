userinput=" >"

print("Note: Press enter to keep the story lines going.")
input()
print("""You wake up from unconciousness in a remote laboratory.
You're wearing a lab coat with a badge that says \"Level 4 personnel.\"
You suddenly hear screams and running noises coming closer and closer.
Quick, what do you grab?""")
print("\n1. Sidearm bat stick.\n2. Pepper spray.\n3. Riot shield.")
StartingItem=input(userinput)

if StartingItem == "1":
    print("You take up the bat and get ready to swing.")
    input()
    print("Several rabid infected burst through the door.")
    input()
    print("You take out two of them before being overrun. Good job!")
elif StartingItem == "2":
    print("You take up the can of pepper spray and get ready.")
    input()
    print("Several rabid infected burst through the door.")
    input()
    print("You empty the whole can at them but to no effect. Good job!")
elif StartingItem == "3":
    print("You pick up the heavy plastic shield and position yourself.")
    input()
    print("Several rabid infected burst through the door.")
    input()
    print("You gave a shout and plowed through them at full force.")
    input()
    print("Now that you're out of the room, where do you go?")
    print("1. Go left where the lights are flickering but the walls are clean.")
    print("2. Go right where the lights are perfectly on but the walls are splattered with blood.")

    WhereTo=input(userinput)
    if WhereTo == "1":
        print("You go left carrying the shield with you.")
        input()
        print("You come across a room with the door locked. Next to it there's a scanner device.")
        input()
        print("Remembering your level 4 badge, you held it in front of the scanner.")
        input()
        print("The door swings open silently, revealing an empty room with a wall full of screens.")
        input()
        print("You realize that this is the surveillance room and you can see everything in the facility.")
        print("You quickly remember to close the door behind you and you do so.")
        print("The door is extremely heavy and thick so you're safe for now.")
        input()
        print("Good job! You win! Stay tuned for part 2?")
    elif WhereTo == "2":
        print("You go right carrying the shield with you.")
        input()
        print("As you went around a corner, there was a group of infected waiting for you!")
        input()
        print("You die a gruesome and grisly death. Good job!")
    else:
        print("You're not funny. Play again.")
