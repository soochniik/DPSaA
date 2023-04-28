def maxPerimetr(arr): #треугольник с максимальным периметром
    maxPer = 0
    for i in range (len(arr) - 2):
        for j in range (i+1, len(arr) - 1):
            for k in range (j+1, len(arr)):
                a = arr[i]
                b = arr[j]
                c = arr[k]
                if (a + b > c and a + c > b and b + c > a and a + b + c > maxPer):
                    maxPer = a + b + c
    return(maxPer)

def maxNum(nums): #максимальное число
    numsStr = []
    res = ""
    for i in nums:
        numsStr.append(str(i))
    numsStr.sort() #сортировка массива строк
    for cur in numsStr: #вставка каждого числа либо в конец, либо в начало
        if cur + res > res + cur:
            res = cur + res
        else:
            res += cur
    return res

def sortDiag(matrix): #сортировка диагоналей в матрице
    m = len(matrix) #кол-во строк
    n = len(matrix[0]) - 1 #кол-во столбцов - 1
    diag = [] #массив для хранения отсортированных диагоналей
    for i in range(2-m, n): #цикл по кол-ву диагоналей (кроме первой и последней)
        for j in range (m):
            if (i + j >= 0 and i + j <= n):
                diag.append(matrix[j][i + j])
        diag.sort()
        k = 0
        for j in range (m): #обновление матрицы отсортированными диагоналями
            if (i + j >= 0 and i + j <= n):
                matrix[j][i + j] = diag[k]
                k+=1
        diag = []
    return matrix

print(maxPerimetr([3,2,3,4]))
print(sortDiag([[11, 25, 66, 1, 69, 7], [23, 55, 17, 45, 15, 52], [75, 31, 36, 44, 58, 8], [22, 27, 33, 25, 68, 4], [84, 28, 14, 11, 5, 50]]))
print (maxNum([3,30,34,5,9]))