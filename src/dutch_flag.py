def dutch_flag_sort(balls):
    low, mid, high = 0, 0, len(balls)-1
    while mid<high:
        color=balls[mid]
        if color=="R":
            balls[mid],balls[low]=balls[low],balls[mid]
            low+=1
            mid+=1
        elif color=="B":
            balls[high],balls[mid]=balls[mid],balls[high]
            high-=1
        else:
            mid+=1
    return balls

print(dutch_flag_sort(['G','B','G','G','R','B','R','G']))
