x = input("Enter a Word or Sentance:")

def max_letter(x):
    m,n = 0,0
    for i in range(len(x)):
        n = ord(x[i])
        if n > m:
            m = n
    return m
print(chr(max_letter(x)))
