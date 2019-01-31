# 1월 월말평가 문제예시 
# 예시문제 1. 도형만들기

class Point:
    
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        

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