sum = 0 
valid_strings = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# with open("input.txt", "r") as file: 

#     for line in file: 
#         string_number_list = []
#         for c in line: 
#             if c.isnumeric(): 
#                 string_number_list.append(c) 

#         curr_line = string_number_list[0] + string_number_list[-1]
#         print(curr_line)
#         sum += int(curr_line)

# print(sum)
            

with open("input.txt", "r") as file: 

    for line in file: 

        curr_line = ''

        # create lists needed

        items = [] 
        first_word_occurances = [line.find(x) for x in valid_strings]
        last_word_occurances = [line.rfind(x) for x in valid_strings]

        print(last_word_occurances)

        # find the first occurance of a word number
        min_word_occurance = min(first_word_occurances)
        min_word_occurance_index = first_word_occurances.index(min_word_occurance)

        # find the last occurance of a word number
        max_word_occurance = max(last_word_occurances)
        max_word_occurance_index = last_word_occurances.index(max_word_occurance)

        # min_number_index = 0
        # max_number_index = len(line)-1
        # max_number = 0

        # reversed_line = line[::-1]

        # for c in line:
        #     if c.isnumeric():
        #         break
        #     min_number_index += 1

        # for c in reversed_line:
        #     if c.isnumeric():
        #         break
        #     max_number_index -= 1
        #     max_number += 1

        # if min_word_occurance < min_number_index:
        #     curr_line += str(numbers[min_word_occurance_index])
        # else: 
        #     curr_line += line[min_number_index]

        # if max_word_occurance > max_number_index:
        #     curr_line += str(numbers[max_word_occurance_index])
        # else: 
        #     curr_line += line[max_number]

        # print(curr_line)

       
        
        item_index = 0 
        is_word = False
        for c in line:
            if c.isnumeric():
                break
            item_index += 1

        for index, item in enumerate(first_word_occurances): 
            if item < item_index and item != -1:
                is_word = True
                curr_line += str(numbers[index])

        if not is_word: 
            curr_line += line[item_index]

        

        # get index of max word occurance

        max_word_occurance = max(last_word_occurances)
        max_word_occurance_index = last_word_occurances.index(max_word_occurance)

        item_index = len(line)-1
        number = 0
        is_word = False
        reversed_line = line[::-1]

        for c in reversed_line: 
            if c.isnumeric():
                break
            item_index -= 1
            number += 1

        print(max_word_occurance)
        if max_word_occurance > item_index:
            is_word = True
            curr_line += str(numbers[max_word_occurance_index])
            sum += int(curr_line)

        else: 

            for c in reversed_line: 
                if c.isnumeric():
                    curr_line += c
                    break
            sum += int(curr_line)

        if int(curr_line) > 99:
            print(line)
            print(curr_line)
        

print(sum)