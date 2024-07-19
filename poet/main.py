from os import path
import random

def	parse_words():
	sustantives =	(open("poet/sources/ms_sustantives.txt").read().split('\n'),
							open("poet/sources/mp_sustantives.txt").read().split('\n'),
							open("poet/sources/fs_sustantives.txt").read().split('\n'),
							open("poet/sources/fp_sustantives.txt").read().split('\n'))

	conectors =		(open("poet/sources/s_conectors.txt").read().split('\n'),
							open("poet/sources/p_conectors.txt").read().split('\n'))

	adjectives = 	(open("poet/sources/ms_adjectives.txt").read().split('\n'),
					  		open("poet/sources/mp_adjectives.txt").read().split('\n'),
							open("poet/sources/fs_adjectives.txt").read().split('\n'),
							open("poet/sources/fp_adjectives.txt").read().split('\n'))
	return (sustantives, conectors, adjectives)

def generateLine(words: tuple):
	genero = random.randint(0, 3)
	sustantivo = random.randint(0, words[0][genero].__len__() - 1)
	conector = random.randint(0, words[1][genero % 2].__len__() - 1)
	adjetivo = random.randint(0, words[2] [genero].__len__() - 1)
	if random.randint(1, 2) == 1:
		adjetivo2 = random.randint(0,  words[2][genero].__len__() - 1)
		line = words[0][genero][sustantivo] + ' ' + words[2][genero][adjetivo] + ' ' + words[1][genero%2][conector] + ' ' + words[2][genero][adjetivo2]
	else:
		sustantivo2 = random.randint(0, words[0][genero].__len__() - 1)
		line = words[0][genero][sustantivo] + ' ' + words[2][genero][adjetivo] + ' ' + words[1][genero%2][conector] + ' ' + words[2][genero][sustantivo]
	return (line)

def	poet(token, numberOfLines):
	words = parse_words()
	for i in range (0, numberOfLines):
		print(generateLine(words))