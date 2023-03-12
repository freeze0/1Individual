#dsa9731das5861dsa5g6fdh7898bsddfj445kjg8cxv395nf8m6g54dg3516gh7jbvn85kugil56rsg3fd4gcbvn386iguy534sdaf2470
#составление словаря с парой (число, количество вхождений числа в строку)
stroka = 'a2b5c6jja8j6k49hs856j11k6k8k3nvj46k0'
chisla = dict()
for i in stroka:
    if i.isdigit():
        if i not in chisla:
            chisla[int(i)] = stroka.count(i)

#сортировка по возрастанию
chisla = dict(sorted(chisla.items(), key=lambda x: x[0]))
chisla.pop(0)
print(chisla)
otvet = ''

#составление числа и нахождение минимального числа которое можно поставить в центр
min = 10
for key, value in chisla.items():
    _value = value / 2
    if key < min and value % 2 != 0:
        min = key
    while _value >= 1:
        otvet += str(key)
        _value -= 1
print(min)
print(otvet, min, otvet[::-1])
