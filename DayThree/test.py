import re

with open("input.txt", "r") as file:

    temp_str = ''

    for line in file:

        temp_str += line

    numbers = re.findall(r'(?<=\W)\d+|\d+(?=\W)', temp_str)

    total = sum(map(int, numbers))

    print (total)