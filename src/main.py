#Main game file

import zork
loop='Start Room'
while True:
    while loop=='North Room':
        if loop=='North Room':
            print("---------------------------------------------------------")
            print("You find yourself at the edge of a beautiful lake aside rolling hills.")
            print("A small pier juts out into the lake.")
            print("A fishing rod rests on the pier.")
            print("(You can see a white house in the distance to the south.)")
            north_house_inp = input("What do you do? ")
            list_list=zork.NorthRoom(north_house_inp)
            loop=list_list[0]
            print('You are in the ' + list_list[0] + ', and you are ' + list_list[1])
    while loop=='Start Room':
        if loop=='Start Room':
            print("---------------------------------------------------------")
            print("You are standing in an open field west of a white house, with a boarded front door.")
            print("You can see a small lake to the north.")
            print("(A secret path leads southwest into the forest.)")
            print("There is a Small Mailbox.")
            second = input("What do you do? ")
            list_list=zork.Room0(second)
            loop=list_list[0]
            print('You are in the ' + list_list[0] + ', and you are ' + list_list[1])
    while loop=='Southwest Room':        
        if loop=='Southwest Room':
            print("---------------------------------------------------------")
            print("This is a forest, with trees in all directions. To the east, there appears to be sunlight.")
            forest_inp = input("What do you do? ")
            list_list=zork.SouthwestRoom(forest_inp)
            loop=list_list[0]
            print('You are in the ' + list_list[0] + ', and you are ' + list_list[1])
    while loop=='East Room':
        if loop=='East Room':
            print("---------------------------------------------------------")
            print("You are in a clearing, with a forest surrounding you on all sides. A path leads south.")
            print("There is an open grating, descending into darkness.")
            grating_inp = input("What do you do? ")
            list_list=zork.EastRoom(grating_inp)
            loop=list_list[0]
            print('You are in the ' + list_list[0] + ', and you are ' + list_list[1])
    while loop=='Cave Room':
        if loop=='Cave Room':
            print("---------------------------------------------------------")
            print("You are in a tiny cave with a dark, forbidding staircase leading down.")
            print("There is a skeleton of a human male in one corner.")
            cave_inp = input("What do you do? ")
            list_list=zork.CaveRoom(cave_inp)
            loop=list_list[0]
            print('You are in the ' + list_list[0] + ', and you are ' + list_list[1])
    while loop=='End Room':
        if loop=='End Room':
            print("---------------------------------------------------------")
            print("You have entered a mud-floored room.")
            print("Lying half buried in the mud is an old trunk, bulging with jewels.")
            last_inp = input("What do you do? ")
            list_list=zork.EndRoom(last_inp)
            loop=list_list[0]
            print('You are in the ' + list_list[0] + ', and you are ' + list_list[1])
    while loop=='Back of House':
        if loop=='Back of House':
            print("---------------------------------------------------------")
            print('You find yourself on the back side of the white house')
            print('West of where you are there is a old worn down window')
            house_imp=input("What do you do ")
            list_list=zork.BackofHouseRoom(house_imp)
            loop=list_list[0]
            print('You are in the ' + list_list[0] + ', and you are ' + list_list[1])
    while loop=='Kitchen':
        if loop=='Kitchen':
            print("---------------------------------------------------------")
            print('You find yourself in a dimly lit kitchen with dust covering the floor.')
            print('A lantern rests on the kitchen island and there is a staircase leading downstairs.')
            print('A set of stairs leads up to another room.')
            kitchen_imp=input("What do you do ")
            list_list=zork.Kitchen(kitchen_imp)
            loop=list_list[0]
            print('You are in the ' + list_list[0] + ', and you are ' + list_list[1])
    while loop=='Attic':
        if loop=='Attic':
            print("---------------------------------------------------------")
            print('You are now in a dimley lit attic space filled with cob webs')
            print('There is a small table with a book on the table')
            attic_imp=input("What do you do ")
            list_list=zork.Attic(attic_imp)
            loop=list_list[0]
            print('You are in the ' + list_list[0] + ', and you are ' + list_list[1])
    while loop=='Maze Entrance':
        if loop=='Maze Entrance':
            print("---------------------------------------------------------")
            print("This is the entrance to a maze. The maze is made up of large green hedges'")
            print("North you see a what looks like a cave")
            print("Looking South you see more maze and more darkness")
            maze_imp=input("What do you do ")
            list_list=zork.MazeEntrance(maze_imp)
            loop=list_list[0]
            print('You are in the ' + list_list[0] + ', and you are ' + list_list[1])
    while loop=='Maze Interior':
        if loop=='Maze Interior':
            print("---------------------------------------------------------")
            print("You are now in the maze")
            print('You can barley see anything and it looks like the maze keeps getting darker')
            mazeent_imp=input("What do you do ")
            list_list=zork.MazeInterior(mazeent_imp)
            loop=list_list[0]
            print('You are in the ' + list_list[0] + ', and you are ' + list_list[1])
    while loop=='Basement':
        if loop=='Basement':
            print("---------------------------------------------------------")
            print('You are in a small dark room')
            print("The staircase you came down are to your right and a lantern in the middle of the room")
            print("There is a door across the room")
            basement_imp=input("What do you do ")
            list_list=zork.Basement(basement_imp)
            loop=list_list[0]
            print('You are in the ' + list_list[0] + ', and you are ' + list_list[1])
            
            
    


