import unittest
from triple import find_pairs, find_sequential_duplicates, clean_string

class DupsTest(unittest.TestCase):
    def test_clean_string(self):
        self.assertEqual(clean_string("Hello, I like nuts. Do you like nuts? No? Are you sure?\n Why don't you like nuts? Are you nuts? I like you"), 'hello i like nuts do you like nuts no are you sure  why don\'t you like nuts are you nuts i like you')

    def test_find_sequential_duplicates(self):
        #Test the given string
        self.assertEqual(find_sequential_duplicates("Hello, I like nuts. Do you like nuts? No? Are you sure?\n Why don't you like nuts? Are you nuts? I like you"), 
                [[1, 2, 3, 5, 6, 7, 9, 10, 15, 16, 17, 18, 19, 20, 21, 22, 23], ['i', 'like', 'nuts', 'you', 'like', 'nuts', 'are', 'you', 'you', 'like', 'nuts', 'are', 'you', 'nuts', 'i', 'like', 'you']]) 
        #Test orphaned duplicate
        self.assertEqual(find_sequential_duplicates("Hello, I like nuts. Heat nuts fire. Do you like nuts? No? Are you sure?\n Why don't you like nuts? Are you nuts? I like you"), 
               [[1, 2, 3, 8, 9, 10, 12, 13, 18, 19, 20, 21, 22, 23, 24, 25, 26], ['i', 'like', 'nuts', 'you', 'like', 'nuts', 'are', 'you', 'you', 'like', 'nuts', 'are', 'you', 'nuts', 'i', 'like', 'you']]) 
        #Test orphaned duplicate creating a non-dupe
        self.assertEqual(find_sequential_duplicates("Hello, I like nuts. Heat hello fire. Do you like nuts? No? Are you sure?\n Why don't you like nuts? Are you nuts? I like you"), 
            [[1, 2, 3, 8, 9, 10, 12, 13, 18, 19, 20, 21, 22, 23, 24, 25, 26], ['i', 'like', 'nuts', 'you', 'like', 'nuts', 'are', 'you', 'you', 'like', 'nuts', 'are', 'you', 'nuts', 'i', 'like', 'you']])               

    def test_find_pairs(self):
        self.assertEqual(find_pairs("Hello, I like nuts. Heat hello fire. Do you like nuts? No? Are you sure?\n Why don't you like nuts? Are you nuts? I like you"), 
            [[1, 2, 3, 8, 9, 10, 12, 13, 18, 19, 20, 21, 22, 23, 24, 25, 26], ['i', 'like', 'nuts', 'you', 'like', 'nuts', 'are', 'you', 'you', 'like', 'nuts', 'are', 'you', 'nuts', 'i', 'like', 'you']])               



if __name__ == '__main__':
        unittest.main()
