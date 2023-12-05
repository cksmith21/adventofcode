sum = 0
blocks = {"red" : 12, "green" : 13, "blue" : 14 }

with open("input.txt", "r") as file: 

    for line in file: 

        isValid = True

        items = line.split(":")
        game_number = int((items[0].split(" "))[1])

        games = items[1].split(";")

        for game in games: 

            smaller_game = game.strip().split(",")

            for sg in smaller_game: 

                smallest_game = sg.strip().split(" ")

                if int(smallest_game[0]) > blocks[smallest_game[1]]:

                    isValid = False

        if isValid:
            sum += game_number

sum = 0

with open("input.txt", "r") as file: 

    for line in file: 

        min_cubes = [0, 0, 0]
        items = line.split(":")
        games = items[1].split(";")
        power_set = 1

        for game in games: 

            power_set = 1

            smaller_game = game.strip().split(",")

            for sg in smaller_game: 

                smallest_game = sg.strip().split(" ")

                if smallest_game[1] == "red":

                    if int(smallest_game[0]) > min_cubes[0]: 

                        min_cubes[0] = int(smallest_game[0])

                elif smallest_game[1] == "green":

                    if int(smallest_game[0]) > min_cubes[1]: 

                        min_cubes[1] = int(smallest_game[0])

                elif smallest_game[1] == "blue":

                    if int(smallest_game[0]) > min_cubes[2]: 

                        min_cubes[2] = int(smallest_game[0])

                else:
                    
                    pass

        for x in min_cubes:
            if x == 1000:
                power_set *= 1
            else:
                power_set *= x

        sum += power_set

print(sum)