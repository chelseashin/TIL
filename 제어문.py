
'''
Q1
# 자연수 n이 주어졌을 때, 1부터  N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오
'''

# item = int(input("번호를 입력하세요 : "))
# for i in item : 
# print(i+1)

# item = int(input("번호를 입력하세요 : "))
# for i in range(1, item + 1):
#     print(i)

'''
Q2
투자 경고 종목 리스트가 있을 때, 사용자로부터 종목명을 입력받은 후 해당 종목이 
투자 경고 종목이라면 '투자 경고 종목입니다'를 아니면
"투자경고 종목이 아닙니다"를 출력하는 프로그램을 작성하라
'''

# warn.investment_list = ["microsoft", "google", "naver", "kakao", "samsung", "lg"]
# print(f"경고 종목 리스트 : {warn_investment_list}")
# item = input("투자종목이 무엇입니까? : ")

#  if item.lower() in warn.investment_list:
#       print("투자 경고 종목입니다.")
#    else :
#       print("투자 경고 종목이 아닙니다.")

# .lower() : 입력값에 대문자가 들어와도 소문자로 바꿔주는 것.
# if - not in 일 때는 논리구조가 반대로 된다.






# 다음 리스트에서 0, 4, 5번째 항목을 제외한 리스트를 출력하시오
# 방법 1
# colors = ["apple", "banana", "cocont", "deli", "ele", "grape"]
# fruit = []
# deleteindex = [0, 4, 5]

# for i in range(0, len(colors)):
#     if i not in deleteindex:
#         fruit.append(colors[i])
# print(fruit)

# 방법 2
# colors = ["apple", "banana", "cocont", "deli", "ele", "grape"]
# fruit = []
# for i in range(0, len(colors)):
#     if i not in [0, 4, 5]
#       pass
#     else :
#        fruit.append(colors[i])
# print(fruit)




# ssafy_dictionary
# ssafy = {
#     "location": ["서울", "대전", "구미", "광주"],
#     "language": {
#         "python": {
#             "frameworks": {
#                 "flask": "micro",
#                 "django": "full-functioning"
#             },
#             "data_science": ["numpy", "pandas", "scipy", "sklearn"]
#         }
#     },
#     "duration": {
#         "semester1": "6월까지"
#     },
#     "classes": {
#         "seoul":  {
#             "lecturer": "john",
#             "manager": "pro",
#         },
#         "daejeon":  {
#             "lecturer": "tak",
#             "manager": "yoon",
#         }
#     }
# }


# print(ssafy)

# ssafy의 semester1의 기간을 출력하세요.
# dict = ["key" : value]
print(ssafy["duration"]["semester1"])

# ssafy의 dictionary 안에 들어있는 '대전'을 출력하세요
print(ssafy["location"][1])

# daejeon의 매니저의 이름을 출력하세요
print(ssafy["classes"]["daejeon"]["manager"])