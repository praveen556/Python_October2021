def fib(n):
    dict = {}

    dict[0]= 1
    dict[1]= 1

    for i in range(2, n+1):
        if i%3 == 0:
            dict[0] = dict[1] + dict[2]
        if (i-1)%3 == 0:
            dict[1] = dict[0] + dict[2]
        if (i-2)%3==0:
            dict[2] = dict[0] + dict[1]
    return dict[n%3]

print(fib(4))
