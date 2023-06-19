output=[]
num1 = int(input('enter the starting number: '))
num2 = int(input('enter the ending number: '))
for i in range(num1,num2):
    if i%2 == 0:
        output.append(i**2)

    else:
        output.append(i**3)

print(output)
    
