def my_strrev(ary):       # ary : 'abcde'
    str = list(ary)       # str = ['a', 'b', 'c', 'd', 'e']
    for i in range(len(str//2)):     # 2로 나눈 몫
        t = ary[i]
        str[i] = str[len(str)-1-i]  # 3
        str[len(ary) - 1 - i] = t
    ary = "".join(str)
    return ary

ary = "abcde"
# print(list(ary))
# print(len(str//2))
ary = my_strrev(ary)
print(ary)

s = "Reverse this strings"
s = s[-1:0:-1]
print(s)