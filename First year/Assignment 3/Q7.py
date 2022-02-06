def fibonacci(num):
    a = 0
    b = 1
    if num < 0:
        print("Incorrect input")
    elif num == 0:
        return 0
    else:
        for i in range(1, num):
            c = a + b
            a = b
            b = c
        return b
print(fibonacci(int(input("Enter "))))
#Soumil Arora testing
