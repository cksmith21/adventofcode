schematics = [[]]
sum = 0 

with open("input.txt", "r") as file: 

    row = 0
    col = 0

    for line in file:
        for c in line: 
            if c != "\n":
                schematics[row].append(c)
        schematics.append([])
        row += 1


print(len(schematics))
print(len(schematics[0]))

for i in range(0, len(schematics)-1):
    num_str = ''
    found_symbol = False
    building_number = False
    for j in range(0, len(schematics[0])):

        print(schematics[i][j])
        #print(found_symbol)
    

        if schematics[i][j].isnumeric(): 
            num_str += schematics[i][j]
            building_number = True
            symbol = ''

            if i-1 >= 0:
                if not schematics[i-1][j].isnumeric() and schematics[i-1][j] != ".":
                    symbol = schematics[i-1][j]
                    found_symbol = True
            
            if j-1 >= 0:
                if not schematics[i][j-1].isnumeric() and schematics[i][j-1] != ".": 
                    symbol = schematics[i][j-1]
                    ound_symbol = True

            if j+1 < len(schematics[0]):
                if not schematics[i][j+1].isnumeric() and schematics[i][j+1] != ".": 
                    symbol = schematics[i][j+1]
                    found_symbol = True

            if i+1 < len(schematics)-1:
                if not schematics[i+1][j].isnumeric() and schematics[i+1][j] != ".": 
                    symbol = schematics[i+1][j]
                    found_symbol = True

            if i-1 >= 0 and j-1 >= 0: 
                if not schematics[i-1][j-1].isnumeric() and schematics[i-1][j-1] != ".": 
                    symbol = schematics[i-1][j-1]
                    found_symbol = True

            if i+1 < len(schematics)-1 and j+1 < len(schematics[0]): 
                if not schematics[i+1][j+1].isnumeric() and schematics[i+1][j+1] != ".": 
                    symbol = schematics[i+1][j+1]
                    found_symbol = True

            if i-1 >= 0 and j+1 < len(schematics[0]): 
                if not schematics[i-1][j+1].isnumeric() and schematics[i-1][j+1] != ".": 
                    symbol = schematics[i-1][j+1]
                    found_symbol = True

            if i+1 < len(schematics)-1 and j-1 >= 0: 
                if not schematics[i+1][j-1].isnumeric() and schematics[i+1][j-1] != ".": 
                    symbol = schematics[i+1][j-1]
                    found_symbol = True

        if found_symbol and j == len(schematics[0])-1 and schematics[i][j].isnumeric():
            print(num_str)
            print("symbol: " + symbol)
            sum += int(num_str)
            found_symbol = False
            num_str = ''
            
        elif not schematics[i][j].isnumeric() and found_symbol:
            print(num_str)
            print("symbol: " +symbol)
            sum += int(num_str)
            found_symbol = False
            building_number = False
            num_str = ''

        elif schematics[i][j].isnumeric():

            continue

        else: 

            num_str = ''

print(sum)