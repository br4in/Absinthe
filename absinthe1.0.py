#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lxml import html
import sys
from os import system

def sym_crawler(word):
	first_letter = word[0]

	uppercase_letter = first_letter.capitalize()
	lowercase_word = word.lower()
	

	url = 'http://www.ilsinonimo.com/{}/{}/'.format(uppercase_letter, lowercase_word)
	tree = html.parse(url)
	synonyms = tree.xpath('//body//li/*//text()')

	if (len(synonyms) == 0):
		url = 'http://www.ilsinonimo.com/{}/{}/'.format(uppercase_letter, lowercase_word)
		tree = html.parse(url)
		synonyms = tree.xpath('//body//li//text()')
		# Display synonyms 
		line = 1
		#system('clear')
		print('-------------------')
		try:
			for item in synonyms:
				item.encode('ascii', 'ignore')
				print(''.join('[{}] {}'.format(line, item)))
				line += 1
		except UnicodeEncodeError:
			print "'ascii' codec can't encode character u'\xe0'\n -->This has to be fix! <--"
		print('-------------------')

	else:
		# Display synonyms 
		line = 1
		#system('clear')
		print('-------------------')
		try:
			for item in synonyms:
				item.encode('ascii', 'ignore')
				print(''.join('[{}] {}'.format(line, item)))
				line += 1
		except UnicodeEncodeError:
			print "'ascii' codec can't encode character u'\xe0'\n -->This has to be fix! <--"
		print('-------------------')



def getIndex(list1, list2, list3, list4, sentence):
	for index, word in enumerate(list1):
		for i in range(len(list2)):
			print
			if word == list2[i]:
# Replace word with synonyms in the list
				print('Matching : [{}] and [{}] -|- Word : [{}] | Index : [{}]'.format(word, list2[i], word, index))
				for y in range(len(list3)):
					list4[index] = list3[y]
					print list4
					list4 = sentence.split()
			else:
				print('Matching : [{}] and [{}]'.format(word, list2[i]))
	

def showItems(list):
	line = 1
	for word in list:
		print('[{}] {}'.format(line, word))
		line += 1


def words_Picker(list):
	finished = False
	while not finished:
		word = raw_input('Choose the words you want to process. Press <enter> when done: ')
# Check if the input is a valid word from the sentence
		if(len(word) == 0):
			finished = True
		else:
			list.append(word)
			print('Word selected!')
def validity_check(list1, list2):
	for word in list1:
		if word not in list2:
				print('Not a valid word from the sentence!')
				print('Clearing list, enter words again!')
				list2 = []
				words_Picker(list1)


def main():
# Get sentence
	sentence = raw_input('Type sentence : ')
# Split the sentence to access every word by index
	split_sentence = sentence.split()
# Select words to process
	showItems(split_sentence)
# List to hold the words to process
	selected_word = []
# Select words from the sentence
	words_Picker(selected_word)
	validity_check(selected_word, split_sentence)
# Show selected words 
	showItems(selected_word)
# Create new list for replacing words
	new_sentence = sentence.split()

# Start crawling for synonyms
	selected_syms = []
	selected_sym = []
# Create an output file to hold the variants
	with open('Possible variants.txt', 'w') as output_file:
		output_file.write('')

	for word in selected_word:
		system('clear')

		print('Processing word : [{}]'.format(word))
	
		sym_crawler(word)
# Let the user choose from the printed synonyms
		finished = False
		while not finished:
			sym = raw_input('Choose the synonyms you want to process. Press <enter> when done: ')
# Check if the input is a valid word from the sentence
			if (len(sym) == 0):
				finished = True
			else:
				selected_sym.append(sym)
				print('Synonym selected!')
# Show selected words 
		showItems(selected_sym)

		for i in range(len(split_sentence)):
			if word == split_sentence[i]:
				print('//-----------------------//')
				print('Word : [{}] - Index : [{}] in  sentence : [{}]'.format(word, i, sentence))
				print
				print('Possible variants : ')
# Replace words at index
				for y in range(len(selected_sym)):
					new_sentence[i] = selected_sym[y]
					print (" ".join([item for item in new_sentence]))
# Convert new sentence to string
					new_sentence_str = " ".join([item for item in new_sentence])
# Append new sentence to file
					with open('Possible variants', 'a') as output_file:
						output_file.write("{}\n".format(new_sentence_str))
					new_sentence = sentence.split()
				
# Append selected_sym list to selected_syms list
		selected_syms.append(selected_sym)
# Erase the content in the list
		selected_sym = []

def homeScreen():
	system('clear')

	print('\n' * 5)
	banner = '''\
		       _         _       _   _          
		  __ _| |__  ___(_)_ __ | |_| |__   ___ 
		 / _` | '_ \/ __| | '_ \| __| '_ \ / _ |
		| (_| | |_) \__ \ | | | | |_| | | |  __/
		 \__,_|_.__/|___/_|_| |_|\__|_| |_|\___|
	'''
	print(banner)
	print('Absinthe is the Simplest & the Fastest Machine Powered Translation Service.')
	print('')
	print('')
	print('')
	items = ['Find Synonyms', 'Quit']
	items_len = len(items)
	line = 1
	for item in items:
		print('			    [{}] {}'.format(line, item))
		line += 1

	user_choice = raw_input('Enter line number : ')
	if user_choice == '1':
		main()
	elif user_choice == '2':
		quit()
	else:
		print('Error, please type a number between [1] and [{}].'.format(items_len))

	raw_input('Press [Enter] to continue...')
	system('clear')
	print('\n' * 8)

def quit():
	loop = False
	system('clear')
	sys.exit()


# Main Program
loop = True
while loop:
	homeScreen()




