alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
dictAlphabet = {}

str1 = input("Введите строку: ")
key = input("Введите ключ: ")
tab = []
tab1 = []
tab2 = []
dict1 = {}

def cipherSwap(tab, tab2):
    b = 0
    c = 0 #строка
    n = 0 #столбец
    list1 = []
    a = 1
    l = 0
    
    for i in tab[1]:
        list1.append(i)
    list1.sort()

    for i in list1:
        dict1[a] = i
        a += 1
    

    for i in range(len(key)):
        l = dict1[i + 1]
        b = -1
        for i1 in tab2[1]:
            b += 1
            if l == i1:
                for i in range((len(str1) // len(key)) + 2) :
                    tab[c][n] = tab2[c][b]
                    if c == (len(str1) // len(key)) + 1:
                        c = 0
                    else:
                        c += 1
        n += 1
    return tab

def get_key(value):
    for k, v in dictAlphabet.items():
        if v == value:
            return int(k)

def get_value(key):
    for k, v in dict1.items():
        if k == key:
            return int(v)

def qwerty(alphabet, str1, key, dictAlphabet, tab, tab2):
    b = 0
    c = 2
    n = 0
    for i in key:
        tab[0][b] = str(i)
        tab[1][b] = get_key(i)
        b += 1
    for i in str1:
        tab[c][n] = i
        if c == (len(str1) // len(key)) + 1:
            c = 2
            n += 1
        else:
            c += 1
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            tab2[i][j] = tab[i][j]
    return tab, tab2

def createTab(str1, key, tab):
    N = (len(str1) // len(key)) + 2
    M = len(key)
    
    for i in range(N):
        tab.append([0]*M)
    return tab

def addValue(alphabet, dictAlphabet):
    a = 1
    for i in alphabet:
        dictAlphabet[a] = i 
        a += 1

def printMatrix(tab):
    for i in range(len(tab)):         # len(A) - возвращает количество строк в матрице А
        for j in range(len(tab[i])):  # len(A[i]) - возвращает количество элементов в строке i
            print(tab[i][j], end = ' ')
        print()                     # делаем переход на новую строку 


    

tab = createTab(str1, key, tab)
tab2 = createTab(str1, key, tab2)
addValue(alphabet, dictAlphabet)
tab, tab2 = qwerty(alphabet, str1, key, dictAlphabet, tab, tab2)
tab = cipherSwap(tab, tab2)
printMatrix(tab)
