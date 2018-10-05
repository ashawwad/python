Code Kata
https://github.com/PillarTechnology/kata-word-search

Language: python 2.7.15
Dev Environment: Mac 10

Installation:

Python 2.7: Use homebrew to install python 
	$ brew install python

Problem:
Search words in a grid loaded from a csv file (data.csv) and print the location of each word.

Solution Description:
The code written using TDD approach (wite test, fail test, write code, pass test, repeat, refactor)

- Load the data from the csv file
- Split the first row which contains the searched words in a list
- Split the characters from the rest of the rows
- Find a start location where the first character of the search word match a character from the grid
- Navigate the grid from the starting location into the 8 directions
- Compare the 8 words with the searched word, if matched return the location of the characters 


