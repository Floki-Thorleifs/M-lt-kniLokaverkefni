import nltk
import csv
from google import translate
import sqlite3
from sqlite3 import Error
from mybin import getWord

words = []

with open('is-en.txt', encoding='UTF-8') as file:
    csv_reader = csv.reader(file, delimiter='\t')
    for line in csv_reader:
        isl = line[0].split(' ')
        if len(isl) == 2 and ('{' in isl[1] or '[' in isl[1]):
            ens = line[1].split(' ')
            newEns = ''
            for i in ens:
                if '<' not in i:
                    newEns = newEns + i
            words.append((isl[0].lower(), newEns))
newDict = dict(words)

conn = None
try:
    conn = sqlite3.connect('gogn.db')
except Error as e:
    print(e)


""" x = input('Skrifaðu setningu sem á að þýða: ').split(' ')
if x[0] == "":
    x = [x[1]]
while x[0] != 'stop':
    newSent = ''
    for i in x:
        newWord = getWord(i)
        if newWord.lower() in newDict:
            word = newDict[newWord.lower()]
        else:
            word = translate(i.strip(" "))
        # print(i, ' -> ', newWord, ' -> ', word)
        if i[0].isupper():
            word = word.capitalize()
        newSent = newSent + word + ' '
    saves = ""
    finalSent = ""
    newSents = newSent.split(" ")
    for i in newSents:
        if i != saves:
            finalSent = finalSent + i + ' '
        saves = i
    print(finalSent)
    x = input('Skrifaðu setningu sem á að þýða: ').split(' ' )"""


def translateSent(x):
    newSent = ''
    a = x.split(' ')
    for i in a:
        newWord = getWord(i)
        if newWord.lower() in newDict:
            word = newDict[newWord.lower()]
        else:
            word = translate(i.strip(" "))
        # print(i, ' -> ', newWord, ' -> ', word)
        if i[0].isupper():
            word = word.capitalize()
        newSent = newSent + word + ' '
    saves = ""
    finalSent = ""
    newSents = newSent.split(" ")
    for i in newSents:
        if i != saves:
            finalSent = finalSent + i + ' '
        saves = i
    return finalSent
