import items

def Room0(second):
        status='alive'
        if second.lower() == ("take mailbox"):
                print("---------------------------------------------------------")
                print("It is securely anchored.")
                loop='Start Room'
        elif second.lower() == ("open mailbox"):
                print("---------------------------------------------------------")
                print("Opening the small mailbox reveals a leaflet.")
                loop='Start Room'
        elif second.lower() == ("go north"):
                loop = 'North Room'
        elif second.lower() == ("open door"):
                print("---------------------------------------------------------")
                print("The door cannot be opened.")
                loop='Start Room'
        elif second.lower() == ("take boards"):
                print("---------------------------------------------------------")
                print("The boards are securely fastened.")
                loop='Start Room'
        elif second.lower() == ("look at house"):
                print("---------------------------------------------------------")
                print("The house is a beautiful colonial house which is painted white. It is clear that the owners must have been extremely wealthy.")
                loop='Start Room'
        elif second.lower() == ("go southwest"):
                loop = 'Southwest Room'
        elif second.lower() == ("read leaflet"):
                print("---------------------------------------------------------")
                print("Welcome to the Unofficial Python Version of Zork. Your mission is to find a Jade Statue.")
                loop='Start Room'
        elif second.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                status='dead'
                dead_inp = input("Do you want to continue? Y/N ")
                if dead_inp.lower() == ("n"):
                        exit()
                if dead_inp.lower() == ("y"):
                        loop='Start Room'
        else:
                print("---------------------------------------------------------")
                loop='Start Room'
        return [loop,status]
def NorthRoom(north_house_inp):
        status='alive'
        if north_house_inp.lower() == ("go south"):
                loop = 'Start Room'
        elif north_house_inp.lower() == ("swim"):
                print("---------------------------------------------------------")
                print("You don't have a change of clothes and you aren't here on vacation.")
                loop='North Room'
        elif north_house_inp.lower() == ("fish"):
                print("---------------------------------------------------------")
                print("You spend some time fishing but nothing seems to bite.")
                loop='North Room'
        elif north_house_inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                status='dead'
                dead_inp = input("Do you want to continue? Y/N ")
                if dead_inp.lower() == ("n"):
                        exit()
                if dead_inp.lower() == ("y"):
                        loop='Start Room'
                else:
                        print("---------------------------------------------------------")
                        loop='North Room'
        return [loop,status]
def SouthwestRoom(forest_inp):
        status='alive'
        if forest_inp.lower() == ("go west"):
                print("---------------------------------------------------------")
                print("You would need a machete to go further west.")
                loop='Southwest Room'
        elif forest_inp.lower() == ("go north"):
                print("---------------------------------------------------------")
                print("The forest becomes impenetrable to the North.")
                loop='Southwest Room'
        elif forest_inp.lower() == ("go south"):
                print("---------------------------------------------------------")
                print("Storm-tossed trees block your way.")
                loop='Southwest Room'
        elif forest_inp.lower() == ("go east"):
                loop = 'East Room'
        elif forest_inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                status='dead'
                dead_inp = input("Do you want to continue? Y/N ")
                if dead_inp.lower() == ("n"):
                        exit()
                if dead_inp.lower() == ("y"):
                        loop='Start Room'
        else:
                print("---------------------------------------------------------")
                loop='Southwest Room'
        return [loop,status]
 
def EastRoom(grating_inp):
        status='alive'
        if grating_inp.lower() == ("go south"):
                print("---------------------------------------------------------")
                print("You see a large ogre and turn around.")
                loop='East Room'
        elif grating_inp.lower() == ("descend grating"):
                loop='Cave Room'
        elif grating_inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                status='dead'
                dead_inp = input("Do you want to continue? Y/N ")
                if dead_inp.lower() == ("n"):
                        exit()
                if dead_inp.lower() == ("y"):
                        loop='Start Room'                
        else:
                print("---------------------------------------------------------")
                loop='East Room'
        return [loop,status]
def CaveRoom(cave_inp):
        status='alive'
        if cave_inp.lower() == ("descend staircase"):
                loop='End Room'
        elif cave_inp.lower() == ("take skeleton"):
                print("---------------------------------------------------------")
                print("Why would you do that? Are you some sort of sicko?")
                loop='Cave Room'
        elif cave_inp.lower() == ("smash skeleton"):
                print("---------------------------------------------------------")
                print("Sick person. Have some respect mate.")
                loop='Cave Room'
        elif cave_inp.lower() == ("light up room"):
                print("---------------------------------------------------------")
                print("You would need a torch or lamp to do that.")
                loop='Cave Room'
        elif cave_inp.lower() == ("break skeleton"):
                print("---------------------------------------------------------")
                print("I have two questions: Why and With What?")
                loop='Cave Room'
        elif cave_inp.lower() == ("go down staircase"):
                loop ='End Room'
        elif cave_inp.lower() == ("scale staircase"):
                loop ='End Room'
        elif cave_inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                status='dead'
                dead_inp = input("Do you want to continue? Y/N ")
                if dead_inp.lower() == ("n"):
                        exit()
                if dead_inp.lower() == ("y"):
                        loop='Start Room'
        else:
                print("---------------------------------------------------------")
                loop='Cave Room'
        return [loop,status] 
def EndRoom(last_inp):
        status='alive'
        if last_inp.lower() == ("open trunk"):
                print("---------------------------------------------------------")
                print("You have found the Jade Statue and have completed your quest!")
        elif last.inp.lower() == ("kick the bucket"):
                print("---------------------------------------------------------")
                print("You die.")
                print("---------------------------------------------------------")
                status='dead'
                dead_inp = input("Do you want to continue? Y/N ")
                if dead_inp.lower() == ("n"):
                        exit()
                if dead_inp.lower() == ("y"):
                        loop='Start Room'
        else:
                print("---------------------------------------------------------")
        exit_inp = input("Do you want to continue? Y/N ")
        if exit_inp.lower() == ("n"):
                exit()
        if exit_inp.lower() == ("y"):
               loop='Start Room' 
