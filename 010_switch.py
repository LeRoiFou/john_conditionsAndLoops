"""
Dans le programme ci-après, on simplifie les lignes de conditions if / elif / else par un dictionnaire 

Éditeur : Laurent REYNAUD 
Date : 27-11-2020 
"""


def red():
    print('Rouge')


def green():
    print('Vert')


def blue():
    print('Bleu')


def error():
    print('Erreur de saisie')


color = input('Couleur (RGB) : ')

"""Conditions 'classiques' avec les instructions if/elif/else"""
# if color == 'rouge':
#     red()
# elif color == 'vert':
#     green()
# elif color == 'bleu':
#     blue()
# else:
#     error()

"""Simplification des conditions ci-avant en recourant à un dictionnaire"""
d = {'rouge': red, 'vert': green, 'bleu': blue}
func = d.get(color, error)
func()
