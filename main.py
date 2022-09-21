x = 0
if x <= -500:
    print ( f'{x=} Вариант, где x <= -500')
elif x <= -100 and x > -500:
    print ( f'{x=} Вариант, где x <= -100 и  x > -500')
elif x < 0 and x > -100:
    print ( f'{x=} Вариант, где x < 0 и  x > -100')
elif x >= 0 and x < 500:
    print ( f'{x=} Вариант, где x >= 0 и  x < 500')
elif x >= 100 and x < 500:
    print ( f'{x=} Вариант, где x >= 100 и  x < 500')
elif x >= 500:
    print( f'{x=} Вариант, где x >= 500')