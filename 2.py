print('введите номер места')
x = int(input(""))
if x == 0 or x < 0:
    print('неправильный номер')
elif x % 2 == 0 and x <= 36:
    print('верхнее купе')
elif x % 2 != 0 and x <=36:
    print('нижнее купе')
elif x % 2 == 0 and x > 36:
    print('верхнее боковое')
else:
    print('нижнее боковое')