import random


def read_file(filename):
    words = {}
    with open(filename, "r") as file:
        wordList = list(file)

    random.shuffle(wordList) 

    for word in wordList:
        word = word.strip("\n")
        if word not in words:
            words[word] = {"len":len(word)}

    return words

def getPotentialWords(words, maxWord, minWord):
    potentialWords = {}
    for word in words:
        if words[word]["len"] >= minWord and words[word]["len"] <= maxWord:
            potentialWords[word] = len(word)
    return potentialWords

def getPasswords(words, minL, maxL, minWord, maxWord):
    pswdList = []
    usedWords = []
    potentialWords = getPotentialWords(words, maxWord, minWord)

    count = 0
    while count < 10:
        pswd = ""
        pswds = []
        wordSize = maxL
        for word in potentialWords:
            if len(pswd)+potentialWords[word] < minL and word not in usedWords and len(pswds) < 4:
                usedWords.append(word)
                pswd += word
                pswds.append(word)
                wordSize = wordSize - potentialWords[word]
            else:
                if potentialWords[word] < wordSize and word not in usedWords and len(pswds) < 4:
                    usedWords.append(word)
                    pswd += word
                    pswds.append(word)
                    wordSize = wordSize - potentialWords[word]

        if len(pswds) == 4 and len("".join(pswds)) >= minL and len("".join(pswds)) <= maxL:
            pswdList.append(pswds[0]+pswds[1]+pswds[2]+pswds[3])
            pswd = ""
            wordSize = maxL
            count += 1

    return pswdList

def substitution(lst):
    num_subs = {"e":"3", "a":"4","s":"5","b":"8","o":"0"}
    for i in range(len(lst)):
        lst[i] = list(lst[i])
        for j in range(len(lst[i])):
            if lst[i][j] in num_subs:
                lst[i][j] = num_subs[lst[i][j]]
        lst[i] = "".join(lst[i])
    return lst 