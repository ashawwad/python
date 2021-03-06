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

	def get_8_directions(self, word, characters_grid, y,z):
		char_range = range(len(word))
		grid_dimension = len(characters_grid)
		points_in_8directions = [	
						list(map(lambda i: (y-i,z), filter(lambda i: y-i >= 0, char_range))),
						list(map(lambda i: (y+i,z), filter(lambda i: y+i <= grid_dimension-1, char_range))),
						list(map(lambda i: (y,z-i), filter(lambda i: z-i >= 0, char_range))),
						list(map(lambda i: (y,z+i), filter(lambda i: z+i <= grid_dimension-1, char_range))),
						list(map(lambda i: (y-i,z-i), filter(lambda i: y-i>= 0 and z-i >= 0, char_range))),
						list(map(lambda i: (y-i,z+i), filter(lambda i: y-i >= 0 and z+i <= grid_dimension-1, char_range))),
						list(map(lambda i: (y+i,z-i), filter(lambda i: y+i <= grid_dimension-1 and z-i >= 0, char_range))),
						list(map(lambda i: (y+i,z+i), filter(lambda i: y+i <= grid_dimension-1 and z+i <= grid_dimension-1, char_range)))
					 ]

		return points_in_8directions

	def search_word(self, word, characters_grid, y,z):	
		all_directions = self.get_8_directions(word, characters_grid, y,z)
		for direction in all_directions:
			if word == ''.join([characters_grid[row][col] for row,col in direction]):
				return True

		return False

	def search_word_location(self, word, characters_grid, y,z):
		all_directions = self.get_8_directions(word, characters_grid, y,z)
		for direction in all_directions:
			if word == ''.join([characters_grid[row][col] for row, col in direction]):
				return [(row, col) for col, row in direction]

		return []

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

	def find_word_location(self, searched_word):
		characters_grid = self.get_characters_grid_from_file()
		words = self.get_words_grid_from_file()
		grid_dimension = len(characters_grid)
		for i in range(grid_dimension):
			for j in range(grid_dimension):
				if characters_grid[i][j] == searched_word[0]:
					result = self.search_word_location(searched_word, characters_grid, i, j)
					if result:
						return ','.join(map(str, result))

	def print_file_words_with_location(self):
		characters_grid = self.get_characters_grid_from_file()
		words = self.get_words_grid_from_file()
		grid_dimension = len(characters_grid)
		results = []
		for word in words:
			for i in range(grid_dimension):
				for j in range(grid_dimension):
					if characters_grid[i][j] == word[0]:
						result = self.search_word_location(word, characters_grid, i, j)
						if result:
							results.append("{0}: {1}".format(word, ','.join(map(str, result))))

		print("\n".join(results))

if __name__ == '__main__':
	search_class = search_words("data.csv")
	search_class.print_file_words_with_location()
