import sys
import string

def clean_string(input_string):
    removal_map = str.maketrans({
        '\n': ' ',
        '\r': ' ',
        '.': None,
        '$': None,
        '#': None,
        '@': None,
        '?': None,
        '!': None,
        ',': None,
        '(': None,
        ')': None,
        ':': None,
        ';': None
    })
    output_string = input_string.translate(removal_map).lower()  

    return output_string


def find_sequential_duplicates(input_string):
    """Need to find duplicates in the string, remove non-dupes, remove dupes not next to other dupes and their pair dups."""
    strings_list = clean_string(input_string).split(' ')
    duplicates = []
    positions = []
    words = []
    for i, word in enumerate(strings_list):
        if strings_list.count(word) > 1:
            positions.append(i)
            words.append(word)

    zipped_copy = zip(positions, words)
    list_length = len(positions)
    for i, word in zipped_copy:     #Remove non-sequential entries since they can't be pairs
        current_index = positions.index(i)
        last_num = None
        next_num = None
        remove_item = False
        if current_index > 0:
            last_num = positions[current_index - 1]
        if current_index < list_length - 1: 
            next_num = positions[current_index + 1]

        if next_num and last_num:
            if i - last_num != 1 and next_num - i != 1:
                remove_item = True
        else:
            if next_num and next_num - i != 1:
                remove_item = True
            if last_num and i - last_num != 1:
                remove_item = True

        if remove_item:
            del positions[current_index]
            del words[current_index]
            list_length = list_length - 1

    for i, word in enumerate(words):
        if words.count(word) == 1:
            del positions[i]
            del words[i]

    duplicates.append(positions)
    duplicates.append(words)

    return duplicates


def find_pairs(input_string):
    duplicates = find_sequential_duplicates(input_string)
    print(duplicates)
    



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python {} "<input string>"'.format(str(sys.argv[0])))
        exit(1)
    else:
        input_string = str(sys.argv[1])
        find_pairs(input_string)
