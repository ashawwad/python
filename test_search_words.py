import unittest

class test_search_words(unittest.TestCase):

	def test_reading_words_from_file(self):

		self.assertEqual(7, get_words_grid_from_file())

if __name__ == '__main__':
	unittest.main()