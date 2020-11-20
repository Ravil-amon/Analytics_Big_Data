# Запрос выручки и издержки
viruchka = int(input("Выручка фирмы: $"))
izderjki = int(input('Издержки фирмы: $'))
# Финансовый результат
if viruchka > izderjki:
    print('Фирма в прибыли.')
    rent = viruchka / izderjki
    print('Рентабельность: ', rent)
else:
    print('Фирма в убытке.')

numbers = int(input('Численность сотрудников фирмы: '))
pribil_na_odnogo = (viruchka - izderjki) / numbers
print('Прибыль на одного сотрудника: ', pribil_na_odnogo, '$')
