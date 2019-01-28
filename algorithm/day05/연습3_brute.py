def bruteForce(text, pattern): ...

def bruteForce2(text, pattern): ...

text = "TTTAACCA"
pattern = "TTA"
print(f"{bruteForce(text, pattern)}")
print(f"{bruteForce2(text, pattern)}")

# 결국 이 함수를 설명하기 위함!
# 해당 문자열 위치가 처음 나온 위치를 반환함
print(text.find(pattern))

a = "This is a book, This is a computer."
b = "is"
print(a.find(b))      # b가 a에서 처음 등장한 자리
print(a.count(b))     # b가 a에서 등장한 횟수