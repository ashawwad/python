import csv

class search_words:

	def __init__(self, file_name):
		self.file = file_name

	def read_file(self):
		with open(self.file) as file:
			words_data = csv.reader(file, delimiter=",")
			words=[]
			for word_data in words_data:
				words.append(word_data)
		return words

	def get_words_grid_from_file(self):
		words = self.read_file()
		return words[0] 

	def get_characters_grid_from_file(self):
		words = self.read_file()
		return words[1:]

	def find_character(self, character):
		characters_grid = self.get_characters_grid_from_file()
		for row in characters_grid:
			for grid_character in row:
				if character == grid_character:
					return True
		return False

	def find_word_any_direction(self, word):
		return False