n = int(input('Введите целое 3 значное число'))
if (n > 99) and (n < 1000):
    sot = (n // 100)
    des = ((n - (sot * 100)) // 10)
    ed = (n - (sot * 100) - (des * 10))

    summ = (sot + des + ed)
    umnog = (sot * des * ed)
    if (summ > 9) and (summ < 100):
        print('Сумма чисел', n, 'это 2 значное число т.к.', n, '=>', sot, '+', des, '+', ed, '=', summ)
    else:
        print('Сумма чисел', n, 'это не 2 значное число т.к.', n, '=>', sot, '+', des, '+', ed, '=', summ)

    if (umnog > 99) and (umnog < 1000):
        print('произведение чисел', n, 'это 3 значное число т.к.', n, '=>', sot, '*', des, '*', ed, '=', umnog)
    else:
        print('произведение чисел', n, 'это не 3 значное число т.к.', n, '=>', sot, '*', des, '*', ed, '=', umnog)
else:
    print('Вы ввели не 3 значное число')