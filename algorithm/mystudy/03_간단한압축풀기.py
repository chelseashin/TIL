import sys
sys.stdin = open("간단한압축풀기.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    # print(N)
    print("# {}".format(tc+1))

    new = ""
    for i in range(N):
        C, K = map(str, input().split())
        new += C*int(K)
    # print(new)

    for j in range(len(new)):
        if j % 10 == 9:
            print(new[j], end="")
            print()
        else:
            print(new[j], end="")
    print()

# 다른 풀이
# def main():
#     tc = int(input())
#     for t in range(1, tc + 1):
#         n = int(input())
#
#         ch_list = [0]
#         for i in range(n):
#             line = input().split()
#             ch = line[0]
#             cnt = int(line[1])
#             ch_list += ch * cnt
#
#         print("#" + str(t))
#         for i in range(1, len(ch_list)):
#             if i % 10 == 0:
#                 print(ch_list[i], end='')
#                 print()
#             else:
#                 print(ch_list[i], end='')
#         print()
#
#
# if __name__ == '__main__':
#     main()

# 다른풀이2
# TC = int(input())
# for tc in range(1, TC + 1):
#     N = int(input())
#     data = [[0] * 2 for i in range(N)]
#
#     for i in range(N):
#         data[i][0], cnt = input().split()
#         data[i][1] = int(cnt)
#
#     print("#%d" % tc)
#
#     cnt = 0
#     for i in range(N):
#         for j in range(data[i][1]):
#             print(data[i][0], end='')
#             cnt += 1
#             if cnt % 10 == 0:  print()
#     print()
