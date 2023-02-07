a = int(input('Введіть продажі 1 менеджера: '))
b = int(input('Введіть продажі 2 менеджера: '))
c = int(input('Введіть продажі 3 менеджера: '))
premium = 200
if a>1000:
    zp1: float = oklad+a*0.08
else:
    a <500
zp1 = oklad+a*0.03
else:
    zp1 = oklad+a*0.05
if b>1000:
    zp2 = oklad+b*0.08
else:
    b <500:
zp2 = oklad+b*0.03
else:
    zp2 = oklad+b*0.05
if c>1000:
    zp3 = oklad+c*0.08
else:
    c <500:
zp3 = oklad+c*0.03
else:
    zp3 = oklad+c*0.05
if zp1 > zp2 and zp1 > zp3:
print('Кращій  продажам - 1 менеджер!')
zp1 += 200
if zp2 > zp1 and zp2 > zp3:
print('Кращій по продажам - 2 менеджер!')
zp2 += 200
if zp3 > zp1 and zp3 > zp2:
print('Кращій по продажам - 3 менеджер!')
zp3 +=200
print('Заробітьня плата 1 менеджера ',zp1)
print('Заробітьня плата 2 менеджера ',zp2)tors[operator2]