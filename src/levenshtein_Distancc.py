def  levenshteinDistance(strWord1, strWord2):
    if len(strWord1)==0:
        return len(strWord2)

    if len(strWord2)==0:
        return len(strWord1)

    matrix = [j for j in range(len(strWord2)+1)]

    for i in range(1, len(strWord1)+1):
        prev = matrix[:]
        matrix[0]=num=i
        for j in range(1, len(strWord2)+1):
            if strWord1[i-1]==strWord2[j-1]:
                num = prev[j-1]
            else:
                num=1+min(prev[j],num,prev[j-1])
            matrix[j] = num
    return matrix[-1]


print(levenshteinDistance("kitten","sitting"))
