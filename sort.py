def sortlist (listA):
    for x in range (len(listA)-1,0,-1):
        if listA[i]>listA[i+1]:
            temp = listA[i]
            listA[i] = listA[i+1]
            listA[i+1] = temp

listA = [67, 45, 2, 13, 1, 998]
bubbleSort(listA)
print(listA)

listB= [89, 23, 33, 45, 10, 12, 45, 45, 45]
bubbleSort(listB)
print(listB)

