import unittest
from triple import find_pairs, find_sequential_duplicates, clean_string

original_string="Hello, I like nuts. Do you like nuts? No? Are you sure?\n Why don't you like nuts? Are you nuts? I like you"
orphan_dupe="Hello, I like nuts. Heat nuts fire. Do you like nuts? No? Are you sure?\n Why don't you like nuts? Are you nuts? I like you"
ozy='I met a traveller from an antique land, Who said—“Two vast and trunkless legs of stone Stand in the desert. . . . Near them, on the sand, Half sunk a shattered visage lies, whose frown, And wrinkled lip, and sneer of cold command, Tell that its sculptor well those passions read Which yet survive, stamped on these lifeless things, The hand that mocked them, and the heart that fed; And on the pedestal, these words appear: My name is Ozymandias, King of Kings; Look on my Works, ye Mighty, and despair!  Nothing beside remains. Round the decay Of that colossal Wreck, boundless and bare The lone and level sands stretch far away.”'
simple = "a a, a a"

class DupsTest(unittest.TestCase):
    def test_clean_string(self):
        self.assertEqual(clean_string(original_string),
              'hello ignr  i like nuts ignr  do you like nuts ignr  no ignr  are you sure ignr  ignr  why don\'t you like nuts ignr  are you nuts ignr  i like you')
        self.assertEqual(clean_string(simple),
              'a a ignr  a a')

    def test_find_sequential_duplicates(self):
        #Test the given string
        self.assertEqual(find_sequential_duplicates(original_string), 
                [
                    [3, 4, 5, 9, 10, 11, 17, 18, 26, 27, 28, 31, 32, 33, 36, 37, 38], 
                    ['i', 'like', 'nuts', 'you', 'like', 'nuts', 'are', 'you', 'you', 'like', 'nuts', 'are', 'you', 'nuts', 'i', 'like', 'you']
                ])

        #Test orphaned duplicate
        self.assertEqual(find_sequential_duplicates(orphan_dupe), 
                [
                    [3, 4, 5, 14, 15, 16, 22, 23, 31, 32, 33, 36, 37, 38, 41, 42, 43], 
                    ['i', 'like', 'nuts', 'you', 'like', 'nuts', 'are', 'you', 'you', 'like', 'nuts', 'are', 'you', 'nuts', 'i', 'like', 'you']
                ])

        self.assertEqual(find_sequential_duplicates(simple), 
                [
                    [0, 1, 4, 5], 
                    ['a', 'a', 'a', 'a']
                ])


    def test_find_pairs(self):
        self.assertEqual(find_pairs(original_string),
                {'are you': 2, 'you like': 3, 'i like': 2, 'like nuts': 3}) 
        self.assertEqual(find_pairs(orphan_dupe),
                {'are you': 2, 'you like': 3, 'i like': 2, 'like nuts': 3}) 
        self.assertEqual(find_pairs(ozy),
                {'on the': 2}) 
        self.assertEqual(find_pairs("a a , a a"),
                {'a a': 2}) 



if __name__ == '__main__':
        unittest.main()
