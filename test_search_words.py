import unittest
from search_words import *

class test_search_words(unittest.TestCase):
	def setUp(self):
		self.search_class = search_words("data.csv")

	def test_reading_words_from_file(self):
		self.assertEqual(7, len(self.search_class.get_words_grid_from_file()))
		
if __name__ == '__main__':
	unittest.main()