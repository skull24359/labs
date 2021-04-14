import itertools

alphabet = "абвгдежзиклмнопрстуфхцчшщьыэюя"
tab = []
tab1 = []
str1 = input("Введите ключ: ")
str1 = ''.join(ch for ch, _ in itertools.groupby(str1))
str2 = ""
print(str1)

def createTab(alphabet):
    N = 5
    M = 6
    count = 0

    for i in range(N):
        tab.append([0]*M)
    
    for i in str1:
        for j in alphabet:
            if i == j:
                alphabet = alphabet.replace(j, '')

    str2 = str1 + alphabet

    for i in range(len(tab)):
        for j in range(len(tab[i])):
            tab[i][j] = str2[count] 
            count += 1
    return tab

def locindex(c): #get location of each character
    loc=list()
    
    for i ,j in enumerate(tab):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc

def cipherPlayfair(tab):
    text = input("Введите сообщение: ")
    text=text.replace(" ", "") 
    i=0
    while i<len(str1):
        loc=list()
        loc=locindex(text[i])
        loc1=list()
        loc1=locindex(text[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(tab[(loc[0]-1)%5][loc[1]],tab[(loc1[0]-1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(tab[loc[0]][(loc[1]-1)%5],tab[loc1[0]][(loc1[1]-1)%5]),end=' ')  
        else:
            print("{}{}".format(tab[loc[0]][loc1[1]],tab[loc1[0]][loc[1]]),end=' ')    
        i=i+2


def printMatrix(tab):
    for i in range(len(tab)):         # len(A) - возвращает количество строк в матрице А
        for j in range(len(tab[i])):  # len(A[i]) - возвращает количество элементов в строке i
            print(tab[i][j], end = ' ')
        print()                     # делаем переход на новую строку 

tab = createTab(alphabet)
printMatrix(tab)
cipherPlayfair(tab)