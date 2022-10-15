def reverse(number):
#convert the number into string
    number = str(number) 
    n = len(number)
    for i in range(0, n, -1):
        print(number[i], end = "")
#output the string in an opposite order
reverse(input("Enter One Num:"))

