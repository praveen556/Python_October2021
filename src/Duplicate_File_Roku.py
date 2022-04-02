import collections

dir_list = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd) 4.txt(xyz)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]

# setting the maxsplit parameter to 1, will return a list with 2 elements!

#output = [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]

buffer  = []
dict = collections.defaultdict()
for path in dir_list:
    temp = path.split(" ")

    for i in range(1, len(temp)):
        temp[i] = str(temp[0])+'/'+str(temp[i])
    if len(temp)==1:
        buffer.append(temp)
    else:
        buffer.append(temp[1:])

for file in buffer:
    for word in file:
        temp = word.split("(")
        if temp[1] not in dict:
            dict[temp[1]]= [temp[0]]
        else:
            dict[temp[1]].append(temp[0])

print(list(dict.values()))
#[['root/a/1.txt', 'root/c/3.txt'], ['root/a/2.txt', 'root/c/d/4.txt', 'root/4.txt'], ['root/c/4.txt']]
