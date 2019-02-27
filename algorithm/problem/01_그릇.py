# plate = input()
# 입력예시 : ()()()(((())()
plate = "()()()(((())()"
# 출력예시 : 120

plates = [i for i in plate]
# print(plates)

height = 10
new = [plates[0]]

for i in range(1, len(plates)):
    if new[-1] == "(":
        if plates[i] == "(":
            new.append(plates[i])
            height += 5
        elif plates[i] == ")":
            new.append(plates[i])
            height += 10

    elif new[-1] == ")":
        if plates[i] == "(":
            new.append(plates[i])
            height += 10
        elif plates[i] == ")":
            new.append(plates[i])
            height += 5
print(height)


# 좋은풀이
# 다음에 들어오는 그릇과 현재 그릇이 같은지 아닌지만 판단하면 됨!
arr = "()()()(((())()"
tot = 10
for i in range(1, len(arr)):
    if arr[i] == arr[i-1]:
        tot += 5
    else:
        tot += 10
print(tot)