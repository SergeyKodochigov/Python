ch = 0
otv = 1
n=1
while n != 0:
    otv = n*otv
    n = int(input('Введите значение'))
    ch+=1
if (ch==1):
    print ('последовательность отсутствует')
else:
    print ('произведение введенных чисел = ', otv)