def print_employees(filename, cohort_number):
    file = open(filename)
    line = file.readline()
    line = 'dummy'
    tab, i = [], 0
    while line:
        line = file.readline()
        tab.append(line.split(','))
        
        print(tab[i][-1])
        i+=1
    return tab

print(print_employees('E:\Personal\Interview KickStart Documents\Roku\employee.txt',1))
