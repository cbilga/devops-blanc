import unittest
import random

from src.main import find_words,create_dictionary

class TestFindInDictionary(unittest.TestCase):
    def test_present(self):
        d=create_dictionary()
        for key, value in d.items():
            max=len(value)-1
            for i in range(10):
                n=random.randrange(max)
                word=list(value)[n]
                pattern=list(word)
                pattern[0]='?'
                pattern=''.join(pattern)
                with self.subTest(f'looking for {pattern}'):
                    self.assertIn(word,','.join(find_words(d,pattern)))
            
    def test_not_present(self):
        d=create_dictionary()
        for key, value in d.items():
            max=len(value)-1
            for i in range(10):
                n=random.randrange(max)
                word=list(value)[n]
                pattern=list(word)
                pattern[0]='#'
                pattern=''.join(pattern)
                with self.subTest(f'looking for {pattern}'):
                    self.assertNotIn(word,','.join(find_words(d,pattern)))

if __name__ == '__main__':
    unittest.main() 
