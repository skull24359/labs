
polib = [["d", "u", "p", "i", "x",],
         ["v", "n", "r", "a", "w",],
         ["z", "f", "m", "h", "t",],
         ["s", "q", "b", "o", "c",],
         ["k", "g", "e", "y", "l"]]

str1 = str(input("Введите строку: "))
str2 = ""
str3 = ""

def cipherPolib(str1, str2):
    for i in str1:
        for i1 in range(len(polib)):
            for j in range(len(polib)):
                if i == polib[i1][j] and i1 == 4:
                    str2 += str(polib[0][j])
                elif i == polib[i1][j]:
                    str2 += str(polib[i1 + 1][j])
    print(str2)
    return str2


def decipherPolib (str2, str3):
    for i in str2:
        for i1 in range(len(polib)):
            for j in range(len(polib)):
                if i == polib[i1][j] and i1 == 0:
                    str3 += str(polib[4][j])
                elif i == polib[i1][j]:
                    str3 += str(polib[i1 - 1][j])
    print(str3)                
        
                
str2 = cipherPolib(str1, str2)
decipherPolib(str2, str3)