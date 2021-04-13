import itertools

alphabet = "абвгдежзиклмнопрстуфхцчшщьыэюя"
tab = []
tab1 = []
str1 = input("Введите строку: ")
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

def cipherPlayfair(tab):
    


def printMatrix(tab):
    for i in range(len(tab)):         # len(A) - возвращает количество строк в матрице А
        for j in range(len(tab[i])):  # len(A[i]) - возвращает количество элементов в строке i
            print(tab[i][j], end = ' ')
        print()                     # делаем переход на новую строку 

tab = createTab(alphabet)
printMatrix(tab)
#clearText()
#convertText()
