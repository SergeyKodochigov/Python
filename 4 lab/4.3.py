n = input('Введите строку')
n1 = n.split()
q = len(n1)
itog = 0
for i in n1:
    z = False
    for j in range(len(i)):
        if (((ord(i[j]) >= ord('а'))) and ((ord(i[j]) <= ord('я')))):
            if z==False and j == len(i)-1:
                itog+=1
        else:
            z = True
            continue
print(itog)