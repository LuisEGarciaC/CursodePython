sum = 0
valores3 = []
valores5 = []
for i in range(20):
    i += 1
    if (i % 3 == 0 or i % 5 == 0):
        sum += i
    if(i % 3 == 0): #agregado valores de 3 
      valores3.append(i)
    elif(i % 5 == 0):  #agregado valores de 5 
      valores5.append(i)
print(str(sum))
print(valores3)
print(valores5)