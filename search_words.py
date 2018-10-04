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

	def search_word(self, word, characters_grid, y,z):
		char_range = range(len(word))
		grid_dimension = len(characters_grid)
		points_in_8directions = [	
						[(y-i,z) for i in char_range if y-i>= 0],#vertical up
						[(y+i,z) for i in char_range if y+i <= grid_dimension-1],#vertical down
						[(y,z-i) for i in char_range if z-i >= 0], #horizontal right
						[(y,z+i) for i in char_range if z+i <= grid_dimension-1],#horizontal left
						[(y-i,z-i) for i in char_range if y-i>= 0 and z-i >= 0],#diagonal up left
						[(y-i,z+i) for i in char_range if y-i >= 0 and z+i <= grid_dimension-1],#diagonal up right
						[(y+i,z-i) for i in char_range if y+i <= grid_dimension-1 and z-i >= 0],#diagonal down left
						[(y+i,z+i) for i in char_range if y+i <= grid_dimension-1 and z+i <= grid_dimension-1]#diagonal down right
					 ]

		for direction in points_in_8directions:
			if word == ''.join([characters_grid[row][col] for row,col in direction]):
				return True

		return False

	def find_word_any_direction(self, searched_word):
		characters_grid = self.get_characters_grid_from_file()
		words = self.get_words_grid_from_file()
		grid_dimension = len(characters_grid)
		for j in range(grid_dimension):
			for i in range(grid_dimension):
				if characters_grid[i][j] == searched_word[0]:
					result = self.search_word(searched_word, characters_grid, i, j)
					if result:
						return True
		return False