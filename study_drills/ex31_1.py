print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Steal the cake.")
    print("2. Grab the cake and throw it at the bear.")
    print("3. Throw a firecracker on the cake.")
    print("4. Call 911.")

    bear = input(" > ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    elif bear == "3":
        print("The firecracker explodes, making the cake vaporize\ninto thin air.")
        print("The bear angrily tears your torso open. Good job!")
    elif bear == "4":
        print("You take out your phone and call 911.")
        print("\"We're sorry, but no one is around to take your call.\"")
        print("The bear looks at you and makes a devilish grin.")
        print("You die two seconds later in a pool of blood. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    print("4. b̷̨̺̍̍̄ẽ̸̹̺͈̈́c̷̜͖̞͒̌̐o̸͚͙̊̚ͅm̷̛̗̏̈́e̷̠̔ ̵̦͗i̷̧͎̖̒̽͊n̷͕̼̲̕s̸̘̩͑̓̈́a̴͖̭͒̈͠n̸̪̉̑̒e̸̹̲͔̐ ")
    print("5. y̸̢̢̛̰̻͙̞̦͇̜͎̘̠͖̦̙͉͂͆̆̈́͗͂̾͠ǫ̶͈͉̞̦̖̝̻̥̲͌͒̐̐̔̃̀̏u̴̡̨̮̪̺͇̭̒͝ͅ'̷̲͕̤̥͔͕̗̪̯̰͙̗͆̆̕r̶̮̎̚ē̸͓̬̲̖͍̦̮̔̐̽̀̓̾̾̀̿̃̐͛̚͝ ̷̹̼̜́̎̎̓̎̀̋̔͘ç̵͈͇̳̙̘̱̿̐̈́̈̾͋͒͐͋̓̇̿̕ȑ̵̭̲̯̹̩̮͎̳͕̙͍̩̬̂̌͑̎͆̌̀ä̸̤̥̖̯̣̼̖̥͚́̉͌̾͊͌͐̐̿̌͠z̴͇̖̘̮̯̳͊͋̄̊ͅy̸̡̡̻̦̺̬̟̬̍̐̊̾̈́̑͘ ̷̮͎̺̗̻̬͓̯̬͈̭͖̯̞̬̞͈͑̏̀̉͑͂n̶͎̠͓̘̏͊́̓̐ố̸̡͙̗̟̈́̀̉̄͒̉̏͊̽̌ẁ̵̨̺͔̺̘̠͐̀͌͆̀͑̂̾̅̋͘̚͝͠.")
    print("6. ++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>+.>+++++++++++..-----------.--.+++++++++++++++++++++++.--------------------.<<++.>>--------------.<++++++++.>+++++++++++++++++++++++++++.------.--------.")


    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")
