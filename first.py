import re
import pickle

try:
    with open('text.txt', 'r') as file:
        data = file.read()
except:
    print("Файл 'text.txt' не найден")
    quit()


def countOfWords():
        count = len(data.split())
        return count


def countOfSentences():
    with open('text.txt') as file:
        count = data.count('.')
        return count


def countOfWordsInSentences():
        strings = data.split('.')
        strings.pop()
        someList = []
        for sent in strings:
            someCort = (sent, len(sent.split()))
            someList.append(someCort)
        return someList


def countInWord():
        dictionary = {}
        words = re.sub(r'[^\w\s]', '', data).split()
        for word in words:
            someWord = []
            someCort = [word, len(word)]
            someWord.append(someCort)
            dictionary.update(someWord)
        return dictionary


def countPunctuation():
        string = data
        znaki = ',.?:;!-'
        dictionary = {}
        someCort = []
        for znak in znaki:
            someCort.append([znak, string.count(znak)])
            dictionary.update(someCort)
        return dictionary


def collectInDict():
    dictionary = {'Всего слов': countOfWords(), 'Всего предложений': countOfSentences(),
                  'Предложения': countOfWordsInSentences(), 'Слова': countInWord(),
                  'Знаки припенания': countPunctuation()}
    return dictionary


def save():
    file = open('someObj.txt', 'wb')
    dictionary = collectInDict()
    pickle.dump(dictionary, file)
    file = open('someObj.txt', 'rb')
    loadedDict = pickle.load(file)

    for key, value in loadedDict.items():
        if(key == 'Всего слов'):
            print(key, value)
        if(key == 'Всего предложений'):
            print(key, value)
        if (key == 'Предложения'):
            print(key)
            i = 1
            for value in loadedDict[key]:
                print('             ' + 'Предложение ' + str(i) + ' |' + str(
                    value[0]) + ' ' + '|количество слов = ' + str(value[1]))
                i += 1
        if (key == 'Слова'):
            print(key)
            for value in loadedDict[key]:
                print('             ' + 'Слово | ' + str(value) + '| его длина = ' + str(loadedDict[key][value]))
        if(key == 'Знаки припенания'):
            print(key)
            for value in loadedDict[key]:
                print('             ' + 'Знак | ' + str(value) + ' | его количество в тексте = ' + str(loadedDict[key][value]))



save()

def breakIntoParagraphs():
    print('Для того чтобы разбить текст на абзацы введите их колличество')
    while True:
        try:
            n = int(input('Введите N: '))
            if(n > 9999 or n < 0):
                print('Число должно быть меньше 9999 и больше 0')
                continue
            else:
                break
        except ValueError:
            print('Вы ввели не число')
            continue
    with open('text.txt') as file:
        sentences = data.split('. ')
        sentences = list(map(lambda s: s if s[-1] == '.' else s + '.', sentences))
        sentences = list(map(lambda s: (s, len(s.split(' '))), sentences))
        paragraphs = [list(map(lambda x: x[0], sentences))[i:i+n] for i in range(0, len(sentences), n)]
        paragraphs = sorted(paragraphs, key=len)
        output = ('\n'.join([' '.join(x) for x in paragraphs]))
    with open('output.txt', 'w') as file:
        file.write(output)
breakIntoParagraphs()