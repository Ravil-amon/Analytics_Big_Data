# Найти самую большую цифру целого числа.
number = int(input('Введите двухзначное число: '))
if number > 9 and number < 100:
    a = number % 10
    b = number // 10
    if a > b:
        print(a, 'больше', b)
    elif a < b:
        print(b, 'больше', a)
    else:
        print('Числа равны.')
else:
    print('Ээээх, просил двухзначное число...:=(')
