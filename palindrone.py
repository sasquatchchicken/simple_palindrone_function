#!/usr/bin/env python3
			#we are creating a fuction to allow the user to enter a word any character length.
			#this entry is case sensitive however a word such as dAd will return True but Dad will return False
word = input('---/\/\ enter your word \n')
def palidrone(word):
	return word == word[::-1] # checking over every char in the word referencing the index till the end
print(palidrone(word))
