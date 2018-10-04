import unittest
from search_words import *

class test_search_words(unittest.TestCase):
	def setUp(self):
		self.search_class = search_words("data.csv")

	def test_reading_words_from_file(self):
		self.assertEqual(7, len(self.search_class.get_words_grid_from_file()))

	def test_list_words_from_file(self):
		self.assertEqual(['BONES', 'KHAN', 'KIRK', 'SCOTTY', 'SPOCK', 'SULU', 'UHURA'],
			self.search_class.get_words_grid_from_file())

	def test_find_character_in_file(self):
		self.assertTrue(self.search_class.find_character('B'))
		self.assertTrue(self.search_class.find_character('K'))
		self.assertFalse(self.search_class.find_character('i'))

	def test_find_word_in_any_directions(self):
		self.assertTrue(self.search_class.find_word_any_direction('BONES'))
		self.assertTrue(self.search_class.find_word_any_direction('SULU'))
		self.assertFalse(self.search_class.find_word_any_direction('PYTHON'))

	def test_find_word_location(self):
		self.assertEqual('(6, 0),(7, 0),(8, 0),(9, 0),(10, 0)', self.search_class.find_word_location('BONES'))
		
if __name__ == '__main__':
	unittest.main()