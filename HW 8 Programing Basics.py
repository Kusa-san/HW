name = "Mohamed Musa"
print(f"Hello, {name}\n")

num1 = 4
num2 = 4

if num1 > num2:
    print(f"{num1} is greater than {num2}\n")
elif num1 < num2:
    print(f"{num2} is greater than {num1}\n")
else:
    print(f"{num1} is equal to {num2}\n")

for i in range (10):
    if i % 2 == 0:
        print(f"{i} is an even number\n")
    else:
        print(f"{i} is an odd number\n")

for i in range (1,10):
    if i % 2 == 0 & i%i == 0:
        print(f"{i} is a prime number\n")