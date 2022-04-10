n=int(input("Enter n: "))

for i in range (n):
    if i%3==0:
        if i%5==0:
            print("Fizz Buzz")
        print("Fizz")
    if i%5==0:
        print("Buzz")
    else:
        print(i)


