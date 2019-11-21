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
enWords = []
with open('en-is.txt', encoding='UTF-8') as file:
    csv_reader = csv.reader(file, delimiter='\t')
    for line in csv_reader:
        en = line[0].split(' ')
        newEn = ''
        if len(en) < 3:
            for i in en:
                if '(' not in i:
                    newEn = newEn + i + ' '
            isl = ''
            for i in line[1].split(' '):
                if '{' not in i and '[' not in i:
                    isl = isl + i
            enWords.append((newEn.lower(), isl.lower()))
enDict = dict(enWords)


def translateSent(x):
    newSent = ''
    a = x.split(' ')
    for i in a:
        newWord = getWord(i)
        if newWord.lower() in newDict:
            word = newDict[newWord.lower()]
        else:
            word = translate(i.strip(" "), 'en', 'isl')
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


def translateEn(x):
    newSent = ''
    a = x.split(' ')
    for i in a:
        if i.lower() in enDict:
            word = enDict[i.lower()]
        else:
            word = translate(i, 'is', 'en')
        newSent = newSent + word + ' '
        print(word)
    saves = ""
    finalSent = ""
    newSents = newSent.split(" ")
    for i in newSents:
        if i != saves:
            finalSent = finalSent + i + ' '
        saves = i
    return finalSent
