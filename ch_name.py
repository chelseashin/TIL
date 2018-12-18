# 파일 이름 변경하기
# dummy 폴더 안에 있는 사람들의 이름 앞에 SAMSUNG 붙이기
# import os
# os.chdir(r"C:\Users\student\Desktop\TIL\dummy")
# for filename in os.listdir("."):
#     os.rename(filename,"SAMSUNG " + filename)

# SAMSUNG이 아니라 SSAFY로 바꾸기!
import os 
os.chdir(r"C:\Users\student\Desktop\TIL\dummy")
for filename in os.listdir("."):
    os.rename(filename, filename.replace("SSAFY SSAFY", "SSAFY"))