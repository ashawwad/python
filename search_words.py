import csv

class search_words:

	def __init__(self, file_name):
		self.file = file_name

	def get_words_grid_from_file(self):
		with open(self.file) as file:
			words_data = csv.reader(file, delimiter=",")
			words=[]
			for word_data in words_data:
				words.append(word_data)
		#[0] for taking the words from first row
		return words[0] 
