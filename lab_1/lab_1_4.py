from math import sqrt

tab = []
str1 = input("Введите текст: ")

if 


def createTab(str1, key, tab):
    N = sqrt(len(str1))
    M = len(key)
    
    for i in range(N):
        tab.append([0]*M)
    return tab