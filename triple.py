import sys
import string

def clean_string(input_string):
    """We can't simply remove punctuation. We need there to be a count difference in the position because one of the rules is that pairs only count if separated by white space."""
    removal_map = str.maketrans({
        '\n': ' ignr ',
        '\r': ' ignr ',
        '.': ' ignr ',
        '$': None,
        '#': None,
        '@': None,
        '?': ' ignr ',
        '!': ' ignr ',
        ',': ' ignr ',
        '(': None,
        ')': None,
        ':': ' ignr ',
        ';': ' ignr '
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
        if word != 'ignr' and word != '' and strings_list.count(word) > 1:
            positions.append(i)
            words.append(word)

    zipped = zip(positions, words)
    list_length = len(positions)
    """Remove non-sequential entries since they can't be pairs"""
    for i, word in zipped:
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

    """Remove dupes that were orphaned by removing non-sequential dupes"""
    for i, word in enumerate(words):
        if words.count(word) == 1:
            del positions[i]
            del words[i]

    if len(positions) == len(words):
        duplicates.append(positions)
        duplicates.append(words)
    else:
        raise ValueError('Words and positions lists are unequal length. Something bad has happened.')
    return duplicates


def find_pairs(input_string):
    """Iterate across list and increment extant pairs and reverse pairs. Then clean out single pairs."""
    duplicates = find_sequential_duplicates(input_string)
    positions = duplicates[0]
    words = duplicates[1]
    pairs = {}
    length = len(positions)

    for i, word in enumerate(words):
        if (i + 1) < length and positions[i + 1] - positions[i] == 1:
            pair = '{} {}'.format(word, words[i + 1])
            pair_reversed = '{} {}'.format(words[i + 1], word)
            if pair not in pairs and pair_reversed not in pairs:
                pairs[pair] = 1
            else:
                if pair_reversed in pairs:
                    pairs[pair_reversed] = pairs[pair_reversed] + 1
                else:
                    pairs[pair] = pairs[pair] + 1

    pairs = dict((k, v) for k, v in pairs.items() if v > 1)
    return pairs


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python {} "<input string>"'.format(str(sys.argv[0])))
        exit(1)
    else:
        input_string = str(sys.argv[1])
        pairs = find_pairs(input_string)
        if pairs:
            for pair, num in pairs.items():
                print('{}: {}'.format(pair, num))
        else:
            print("No pairs found in string.")
