def LongestCPrefix(strs):
    if len(strs)==1:
        return strs[0]

    commonstring = strs[0]

    for i in range(1, len(strs)):
        temp = ''
        j = 0
        while (j <len(commonstring) and j < len(strs[i]) and strs[i][j]==commonstring[j]):
                temp+=strs[i][j]
                j+=1
        commonstring=temp
        if len(commonstring)==0:
            return ''
    return commonstring

print(LongestCPrefix(["ab","a"]))
