# make 1
# f = open("new.txt", "w", encoding='utf-8')
# f.write("What a wonderful world!")
# f.close()

# # make 2
# with open("new.txt", "w") as f:
#     f.write("Hello !!")

# make 1과 2는 같다!

# f = open("new.text", "r")
# data = f.read()
# print(data)
# f.close()

# 몇 번째 줄인지 표시하기
# 방법 1
# f = open("new.txt", "w", encoding = 'utf-8')
# num = list(range(1, 16))
# for i in num:
#     data = f'{i}번째 줄입니다. \n'    
#     f.write(data)
# f.close()

# 방법 2
# f = open("new.txt", "w", encoding = 'utf-8')
# for i in range(5):
#     data = f'{i}번째 줄입니다. \n'    
#     f.write(data)
# f.close()


# 방법 3(with문)
with open("new.txt", "w", encoding = 'utf-8') as f:
    for i in range(10):
        data = f'{i}번째 줄입니다. \n' 
        f.write(data)

# menu 고르기
menu = ["카레\n", "짜장\n", "탕수육\n"]
m =  open("menu.txt", "w", encoding = 'utf-8')
m.writelines(menu)
m.close()

# menu 고르기 2(with문)
menu = ["카레\n", "짜장\n", "탕수육\n"]
with open("menu.txt", "w", encoding = 'utf-8') as f:
	f.writelines(menu)































f = open("line.txt","w", encoding = 'utf-8')
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    words = f'{i}번째입니다.\t'
    f.write(words)
f.close()



with open("ssafy.txt", "w", encoding = 'utf-8') as f:
    for i in range(5):
        data = f'{i}번째 단어\t'
        f.write(data)


















