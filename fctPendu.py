# -*- coding: utf-8 -*-
"""

Created on Fri Dec 10 08:20:17 2021
@author: Augustin Bouveau / Hugues Boisdon
TODO : ALL

"""

from random import randint

def wordChoice():
    fileName = "mots.txt"
    file = open(fileName,'r')
    content = file.readlines()
    word = content[randint(0, len(content))]
    file.close()
    return word.upper().strip()
    
print(wordChoice())
    