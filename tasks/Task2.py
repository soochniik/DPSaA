def winStr(s1, s2): #проверка "победы" некоторой перестановки s1 над s2 и наоборот
    if len(s1) != len(s2):
        return False
    char1 = []
    char2 = []
    for cur in s1:
        char1.append(cur)
    for cur in s2:
        char2.append(cur)
    char1.sort()
    char2.sort()
    i = 0
    while i < len(s1): #проверка "победы" первой строки над второй
        if (char1[i] < char2[i]): #если условие "победы" не выполняется
            break #прерываем цикл, т.к. строки изначально отсортированы
        i += 1
    if (i == len(s1)):
        return True
    i = 0
    while i < len(s2): #проверка "победы" второй строки над первой
        if (char2[i] < char1[i]):
            break
        i += 1
    if (i == len(s2)):
        return True
    else:
        return False
    
def maxPalindrome(str): #максимальная подстрока-палиндром
    mxPal = ""
    for i in range(len(str)):
        curPal = ""
        curPal += str[i]
        if (len(mxPal) == 0):
            mxPal = curPal
        for j in range(i + 1, len(str)):
            curPal += str[j]
            if (curPal == curPal[::-1] and len(curPal) > len(mxPal)): #условие >= для последнего палиндрома, > для первого
                mxPal = curPal
    return mxPal

def substr(str): #кол-во подстрок, представляющих собой конкатенацию 2-х одинаковах строк
    substr = []
    for i in range (len(str)):
        for j in range (i + 1, len(str)):
            if str[j] == str [i]: #если два символа равны
                if str[i:j] == str[j:(2*j-i)]: #если после j-го символа присутствуют такие же, как от i-го до j-го
                    substr.append(str[i:j])
                else:
                    break
    return len(list(set(substr))) #размер множества с уникальными подстроками

print(winStr("abe", "acd"))
print(maxPalindrome("babad"))
print(substr("abcabcabc"))