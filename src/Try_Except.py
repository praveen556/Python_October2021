num = input("Enter a Number:")

try:
    testnum1 = 10*int(num)
    print("Entered Value is a Number")
except:
    print("Entered Value is Character, So coverting it to equivalent Integer:",ord(num))
