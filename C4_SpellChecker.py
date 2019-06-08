from string import *

def calculations(str1, str2):
    cost = 0
    moves = 0
    str1 = str1.lower()
    str2 = str2.lower()
    alphabet = [chr(i) for i in range(97, 123)]
    str1_alphabet = [0 for i in range(0, 26)]
    str1_list = list(str1)
    str2_alphabet = [0 for i in range(0, 26)]
    str2_list = list(str2)

    for index, letter in enumerate(alphabet, start=0):
        for token in str1_list:
            if letter == token:
                str1_alphabet[index] += 1
        for token in str2_list:
            if letter == token:
                str2_alphabet[index] += 1

    result_check([alphabet, str1, str2, str1_list, str2_list, str1_alphabet, str2_alphabet])

    """
    REMOVE FARTHEST LETTERS.
    """
    for index, token in enumerate(str1_alphabet, start=0):
        while token > str2_alphabet[index]:  # We are removing letters.
            str1_alphabet[index] -= 1  # Lower letter count by 1.
            token -= 1
            cost += 20  # Increase cost by 1.
            moves += 1

            if str1_alphabet[index] == 0:
                # Remove the letter if it is guaranteed 100% not in the other string.
                str1_list.remove(alphabet[index])
            else:
                # We need to remove the letter in a position, but the letter we remove should be the farthest away.
                # i.e. again --> aloud. We want to remove the 2nd 'a' from 'again', not the first since it is correct.
                master_index1 = []
                for index2, token2 in enumerate(str1_list, start=0):
                    if token2 == alphabet[index]:
                        master_index1.append(index2)
                master_index2 = []
                for index2, token2 in enumerate(str2_list, start=0):
                    if token2 == alphabet[index]:
                        master_index2.append(index2)
                print(f'Letter: {alphabet[index].upper()}. Master str2: {master_index2}, Master str1: {master_index1}')

                # Find max distances of index.
                max_distance = 0
                remove_index = 0
                for token_index1 in master_index1:
                    for token_index2 in master_index2:
                        if abs(token_index1 - token_index2) > max_distance:
                            max_distance = abs(token_index1 - token_index2)
                            remove_index = token_index1

                # Remove farthest index letter. Least likely to fall into place
                print(f'Max distance is {max_distance} and remove index is {remove_index}')
                del str1_list[remove_index]

    result_check([alphabet, str1, str2, str1_list, str2_list, str1_alphabet, str2_alphabet, cost])
    """
    ADD LETTERS EXACT POSITION.
    """
    while len(str1_list) < len(str2_list):
        str1_list.append('~')

    for index, token in enumerate(str1_alphabet, start=0):
        while token < str2_alphabet[index]:  # We are removing letters.
            str1_alphabet[index] += 1  # Lower letter count by 1.
            token += 1
            cost += 20  # Increase cost by 1.
            moves += 1

            master_index2 = []
            for index2, token2 in enumerate(str2_list, start=0):
                if token2 == alphabet[index]:
                    master_index2.append(index2)

            # Insert letter.
            master_index1 = []
            for index2, token2 in enumerate(str1_list, start=0):
                if token2 == alphabet[index]:
                    master_index1.append(index2)

            print(f'Alphabet: {alphabet[index]} has master index in str2_list = {master_index2}\n'
                  f'master index in str1_list = {master_index1} Inserting letter in str_list at {master_index2[0]}')
            for index2, token_index2 in enumerate(master_index2, start=0):
                try:
                    if master_index2[index2] == master_index1[index2]:
                        continue  # The letters are already perfectly placed.
                    else:
                        str1_list.insert(token_index2, alphabet[index])
                        str1_list.remove('~')
                        break
                except IndexError:
                    str1_list.insert(token_index2, alphabet[index])
                    str1_list.remove('~')
                    break

    remaining_moves = len(str2) - moves
    cost += remaining_moves * 5
    """
    ALL LETTER PERFECTLY MATCH EACH OTHER IN STR_1 AND STR_2.
    SWAP LETTERS UNTIL STR_1 == STR_2
    """

    result_check([alphabet, str1, str2, str1_list, str2_list, str1_alphabet, str2_alphabet, cost])
    return cost


def result_check(print_input):
    print('\n')
    for items in print_input:
        print(f'{items.__class__.__name__} = {items}')
    print('\n')


# TODO: Figure out how on eaRth this is solved using a levenshtein algorithm.
# TODO: Consider expanding this problem by having a list of words from dictionary and finding top 5 closest matching.
# TODO: This algorithm can be expanded to include swapping costs and sparing word-to-word fixed transfer cost.
# The fact that again and against has a cost of 60, rather than 40, seems odd as 4 letters are correctly positioned.
# The textbook problem states that transferring letters is like the river problem, each letter transfer costs 5.

# Case in-sensitive
str_1 = 'algorithm'
str_2 = 'alligator'
min_cost = calculations(str_1, str_2)
print(f'The minimum cost of transforming "Algorithm" to "Alligator" is {min_cost}')
