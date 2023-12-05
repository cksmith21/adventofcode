# part one

sum = 0 
valid_strings = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

with open("input.txt", "r") as file: 

    for line in file: 
        string_number_list = []
        for c in line: 
            if c.isnumeric(): 
                string_number_list.append(c) 

        curr_line = string_number_list[0] + string_number_list[-1]
        print(curr_line)
        sum += int(curr_line)

print(sum)

# part two

number_dict = {"zero": "z0o", "one": "o1e", "two": "t2o", "three": "t3e", 
               "four": "f4r", "five": "f5e", "six": "s6x", "seven": "s7n",
               "eight": "e8t", "nine": "n9e"}
sum = 0          

with open("input.txt", "r") as file: 

    for line in file:

        curr_line = '' 

        for key in number_dict:

            if key in line:

                line = line.replace(key, number_dict[key])

        print(line)

        string_number_list = []
        for c in line: 
            if c.isnumeric(): 
                string_number_list.append(c) 

        curr_line = string_number_list[0] + string_number_list[-1]
        print(curr_line)
        sum += int(curr_line)

print(sum)