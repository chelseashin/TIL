# 1월 월말평가 문제예시 
# 예시문제 1. 도형만들기

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center, r):
        self.center = center
        self.r = r

    # 원의 면적
    def get_area(self):
        return self.r ** 2 * 3.14

    # 원의 둘레
    def get_perimeter(self):
        return self.r * 2 * 3.14 

    # 원의 중점
    def get_center(self):
        return (self.center.x, self.center.y)

    def print(self):
        print(f'circle : {self.get_center()}, r : {self.r}') 

p1 = Point(0, 0) 
c1 = Circle(p1, 3) 
print(c1.get_area()) 
print(c1.get_perimeter()) 
print(c1.get_center()) 
c1.print() 
p2 = Point(4, 5) 
c2 = Circle(p2, 1) 
print(c2.get_area()) 
print(c2.get_perimeter()) 
print(c2.get_center()) 
c2.print()


# 다른 연습
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

# a = FourCal(4, 2)
# print(a.first)
# print(a.second)
# b = FourCal(3, 7)
# # a.setdata(4, 2)
# # b.setdata(3, 7)

# print(a.add())
# print(a.mul())
# print(a.sub())
# print(a.div())

# print(b.add())
# print(b.mul())
# print(b.sub())
# print(b.div())

# .pop(key[, default])
my_dict = {'apple': '사과' , 'banana' : '바나나'}
my_dict.pop('apple')
# print(my_dict)
# error 대신에 0을 리턴
my_dict.pop('melon', 0)

my_dict = {'apple': '사과' , 'banana' : '바나나', 'melon' : '멜론'}
my_dict.update({'pear' : '배'})
# print(my_dict)

# .update()
# key, value 페어 추가하기, key 존재하면 덮어쓰기
my_dict.update({'apple' : '애프으을'})
# print(my_dict)

# .get(key[, default]) : key를 통해 value 가져오기
# my_dict['pineapple'] # 키값이 없으면 에러를 뿜어냄
# print(my_dict.get('pineapple')) # 에러를 뿜지 않음
# print(my_dict.get('pineapple', 0)) # 없으면 0 리턴
# print(my_dict.get('apple'))

# dictionary comprehension
cubic = {i : i ** 3 for i in range(1, 8)}
# print(cubic)

#  다음의 딕셔너리에서 미세먼지 농도가 80 초과 지역만 뽑아 봅시다.
# 예) {'경기': 82, '부산': 90}
dust = {'서울' : 72, '경기' : 82, '대전' : 29, '부산' : 90}
dust_air = {key : value for key, value in dust.items() if value > 80}
# print(dust_air)

# 문제
# 딕셔너리 형태로 언어 및 각 테스트의 결과가 주어지면 테스트 점수가 60 이상인 
# 언어 목록의 결과를 내림차순으로 반환하세요.(중복값은 없습니다)
'''
my_languages({"Java": 10, "Ruby": 80, "Python": 65})
['Ruby', 'Python']
'''
def my_languages(test):
    new = [key for key, value in sorted(test.items(), key=lambda x: x[1], reverse=True) if value >=60]
    return new 

# print(my_languages({"Java": 10, "Ruby": 67, "Python": 89, "PHP": 61}))

# 다음의 딕셔너리에서 미세먼지 농도가 80초과는 나쁨 80이하는 보통으로 하는 value를 가지도록 바꿔봅시다.
# 예) {'서울': '나쁨', '경기': '보통', '대전': '나쁨', '부산': '보통'}
dust = {'서울' : 72, '경기' : 82, '대전' : 29, '부산' : 90}
dust_air = {key:'나쁨' if value > 80 else '보통' for key, value in dust.items()}
dust_air = {key : '매우 나쁨' if value > 150 else '나쁨'
                    if value > 80 else '보통'
                    if value > 30 else '좋음' for key, value in dust.items()}
# print(dust_air)

# map() : map(function, iterable)
a = [1, 2, 3]
# print(''.join(map(str,a)))

a = [1, 2, 3]
b = ''
for i in a:
    b += str(i)
# print(b)

a = [1, 2, 3]
b = ''
for i in range(len(a)):
    b += str(a[i])
# print(b)

# print(''.join([str(x) for x in a]))

a = ['1', '2', '3']
# print(list(map(int, a)))
# print([int(x) for x in a])

class Person:
    name =  "첼씨"
    def sayhello(self):
        print(f"Hello, I'm {self.name}")

iu = Person()
iu.sayhello()
print(iu.name)
iu.name = '채원'
print(iu.name)
iu.sayhello()
print(isinstance(iu, Person))
print(iu)
print(map(int, '123'))

a = (1, 2)
print(a)

b = dict(x = 11, y = 22)
print(b)

c = list(range(10))
c.append(100)
print(c)

print(type(a))
print(type(b))
print(type(c))

iu = Person()
iu.sayhello()
Person.sayhello(iu)

# class Saram:
#     name = 'kim'
#     phone = '01012345678'
#     pocket = {'won' : 500, 'phone' : 1, 'candy' : 5}

#     def in_my_pocket(self, stuff, count):
#         if self.pocket.get(stuff):
#             self.pocket[stuff] += count
#         else:
#             self.pocket[stuff] += count
#         return self.pocket
    
#     def greeting(self):
#         print(f'{self.name}, {self.phone}')

#     def get_my_pocket(self):
#         return self.pocket