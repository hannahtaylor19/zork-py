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
        elif second.lower() == ("go east"):
                loop='Back of House'
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
def Basement(basement_imp):
        status='alive'
        if basement_imp.lower()==('go up staircase'):
                loop='Kitchen'
        elif basement_imp.lower()==('go up stairs'):
                loop='Kitchen'
        elif basement_imp.lower()==('open door'):
                loop='Maze Interior'
        elif basement_imp.lower()==('go through door'):
                loop='Maze Interior' 
        elif basement_imp.lower()==('go up'):
                loop='Kitchen' 
        elif basement_imp.lower()==('pick up lantern'):
                print("---------------------------------------------------------")
                print("Let's go camping! Just kidding, you are looking for someone.. focus!")
                loop='Basement'
        elif basement_imp.lower()==('throw lantern'):
                print("---------------------------------------------------------")
                print("Yes, go ahead break everything why don't ya")
                loop='Basement'
        elif basement_imp.lower()==('smash lantern'):
                print("---------------------------------------------------------")
                print("Ah yes are you the newest member of the WWE? I did not think so")
                loop='Basement'
        elif basement_imp.lower() == ("kick the bucket"):
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
                loop='Basement'
        
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
def BackofHouseRoom(house_imp):
        status='alive'
        if house_imp.lower()==("go south"):
                loop='Maze Entrance'
        elif house_imp.lower()==("go west"):
                print("---------------------------------------------------------")
                print("Opening a rickety window you climb into the  house")
                loop='Kitchen'
        elif house_imp.lower()==("kick the bucket"):
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
                loop='Kitchen'
        return [loop,status]
def Kitchen(kitchen_imp):
        status='alive'
        if kitchen_imp.lower()==('go up stairs'):
                loop='Attic'
        elif kitchen_imp.lower()==('go up'):
             loop='Attic'
        elif kitchen_imp.lower()==('go east'):
                loop='Back of House'
        elif kitchen_imp.lower()==('go down staircase'):
                loop='Basement'
        elif kitchen_imp.lower()==('go down'):
                loop='Basement'
        elif kitchen_imp.lower()==('pick up lantern'):
                print("---------------------------------------------------------")
                print('We are not going camping??')
                loop='Kitchen'
        elif kitchen_imp.lower()==('break lantern'):
                print("---------------------------------------------------------")
                print('But why? Like really why?')
                loop='Kitchen'
        elif kitchen_imp.lower()==('smash lantern'):
                print("---------------------------------------------------------")
                print('You are not the Hulk, okay?')
                loop='Kitchen'
        elif kitchen_imp.lower()==("kick the bucket"):
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
                loop='Kitchen'
        return [loop,status]
def Attic(attic_imp):
        status='alive'
        if attic_imp.lower()==('go down'):
                loop='Kitchen'
        elif attic_imp.lower()==('go down stairs'):
                loop='Kitchen'
        elif attic_imp.lower()==('go down staircase'):
                loop='Kitchen'
        elif attic_imp.lower()==('pick up book'):
                print("---------------------------------------------------------")
                print('Um we are not in English class')
                loop='Attic'
        elif attic_imp.lower()==('throw book'):
                print("---------------------------------------------------------")
                print('So what was the point of that?')
                loop='Attic'
        elif attic_imp.lower()==('open book'):
                print("---------------------------------------------------------")
                print('Welcome to the Unofficial Python Version of Zork. Your mission is to find a Jade Statue.')
                loop='Attic'
        elif attic_imp()==("kick the bucket"):
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
                loop='Attic'
        return [loop,status]
def MazeEntrance(maze_imp):
        status-'alive'
        if maze_imp.lower()==('go north'):
                loop='Cave Room'
        elif maze_imp.lower()==('go south'):
                loop='Maze Interior'
        elif maze_imp.lower()==('look at maze'):
                print("---------------------------------------------------------")
                print('The maze is made out of a drak evergreen bush')
                print('Ivy vines run through the bushses. Darkness seems to come from the maze')
                loop='Maze Enterance'
        elif maze_imp.lower()==('go west'):
                print("---------------------------------------------------------")
                print('A flooded river blocks your path and you are forced to turn around')
                loop='Maze Enterance'
        elif maze_imp.lower()==('go into maze'):
                loop='Maze Interior'
        elif maze_imp.lower()==('enter maze'):
                loop='Maze Interior'
        elif maze_imp.lower()==("kick the bucket"):
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
                loop='Maze Enterance'
        return [loop,status]
        
def MazeInterior(mazeent_imp):
        status='alive'
        if mazeent_imp.lower()==('go north'):
                loop='Maze Entrance'
        else:
                print("---------------------------------------------------------")
                print("The grue attacks and eats you")
                print("You die")
                status='dead'
                dead_inp = input("Do you want to continue? Y/N ")
                if dead_inp.lower() == ("n"):
                        exit()
                if dead_inp.lower() == ("y"):
                        loop='Start Room'
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
        elif cave_inp.lower()==("go south"):
                loop='Maze Enterance'
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
