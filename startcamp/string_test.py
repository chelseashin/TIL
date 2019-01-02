# python 과거
'일은 영어로 %s, 이는 영어로 %s' % ('one', 'two')

# pyformat
'{}, {}'.format('one', 'two')

name = '신채원'
e_name = 'chaewonshin'

print(name, e_name)
print('안녕하세요. {}입니다. My name is {}.'. format(name, e_name))
print('안녕하세요. {0}입니다. My name is {1}.'. format(name, e_name))
print('안녕하세요. {1}입니다. My name is {1}.'. format(name, e_name))


# f-string python 3.6
print(f'안녕하세요. {name}입니다. My name is {e_name}.')


# lotto quiz
import random
num = list(range(1, 46))
print(num)
lotto = sorted(random.sample(num, k = 6))
lotto
print(lotto)

lotto = random.sample(num, k = 6)
lotto.sort()
print(lotto)

name = "신채원"
print("안녕하세요." + name + "입니다." )

# lotto quiz2
print(num)
lotto2 = sorted(random.sample(num, k = 6))
lotto2
print(f'로또 이번주 당첨번호는 {lotto2}입니다.')