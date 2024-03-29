import csv
from google import translate
from sqlite3 import Error
from mybin import getWord

words = []
# Les inn gögnin fyrir ísl->ensk
with open('is-en.txt', encoding='UTF-8') as file:
    csv_reader = csv.reader(file, delimiter='\t')
    for line in csv_reader:
        isl = line[0].split(' ')
        if len(isl) < 3:
            ens = line[1].split(' ')
            newEns = ''
            for i in ens:
                if '<' not in i and '[' not in i:
                    newEns = newEns + i
            words.append((isl[0].lower(), newEns))
# Bý til dictionary úr þeim
newDict = dict(words)
enWords = []
# Les inn gögnin fyrir ensk->ísl
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
# Bý til dictionary
enDict = dict(enWords)


egg = [105, 102, 32, 108, 121, 107, 107, 106, 97]
paskar = ''
for i in egg:
    paskar = paskar + chr(i)
what = [105,102,32,115,116,97,116,101,109,101,110,116]
bunny = ''
for a in what:
    bunny = bunny + chr(a)
basket = [105,102,32,108,111,111,112]
kanina = ''
for s in basket:
    kanina = kanina + chr(s)
karfa = [105,102,32,115,101,116,110,105,110,103]
easter = ''
for k in karfa:
    easter = easter + chr(k)

#Fall sem að tekur inn streng og skílar þýðingu á honum
# Kallar á tvö önnur föll.
# Ef að orðið er ekki í gögnunum mínum þá næ ég í stofnorð orðsins
# á bin og tékka hvort það sé í gögnunum mínum.
# Ef ekki kalla það á google translate fallið sem ég gerði og
# það skilar þýðingu á orðinu
def translateSent(x):
    if x.lower() == paskar:
        return bunny
    newSent = ''
    a = x.split(' ')
    for i in a:
        if i.lower() in newDict:
            word = newDict[i.lower()]
        else:
            newWord = getWord(i)
            if newWord.lower() in newDict:
                word = newDict[newWord.lower()]
            else:
                word = translate(i.lower(), 'en', 'is')
        if i.istitle():
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

# Þýðingar fall fyrir ensku
# Sleppi allri bín vinnslu í þessu og tékka bara beint hvort orðið sé 
# í ensku dictionary sem ég gerði, ef ekki þá nota ég google translate.
def translateEn(x):
    if x.lower() == kanina:
        return easter
    newSent = ''
    a = x.split(' ')
    for i in a:
        if i.lower() in enDict:
            word = enDict[i.lower()]
        else:
            word = translate(i, 'is', 'en')
        newSent = newSent + word + ' '
    saves = ""
    finalSent = ""
    newSents = newSent.split(" ")
    for i in newSents:
        if i != saves:
            finalSent = finalSent + i + ' '
        saves = i
    return finalSent
