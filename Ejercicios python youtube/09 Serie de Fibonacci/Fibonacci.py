sum = 0
num1 = 0
num2 = 1
valores = []
while num2 < 4000000:
    temp = num1
    num1 = num2
    num2 = num2 + temp
    if (num1 % 2 == 0):
        valores.append(num1)
        sum += num1

print(sum)
print(f'valores valores de la serie que estan por debajo de los 4000000 son {valores}')