num = int(input("Enter number : "))
power = int(input("Enter exponent value : "))

result=num

for i in range(power-1):
    result = num * result

print("Result =", result)