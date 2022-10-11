import random
import os

def YeahSan():      # 예산 구성
    global bedgit
    bg = int(input("자신의 예산을 기입하세요. :"))
    bedgit = bg

def batting():      # 베팅할 금액을 정함
    global b
    global bedgit
    b = int(input("배팅할 금액을 입력하세요: "))
    bedgit -= b
    if bedgit <= b:
        print("당신의 예산을 뛰어넘었습니다!")
        exec(open("gamble.py").read())
        exit()
    else:
        pass

def gamble():       # 도박 시스템 구성
    global b
    global bedgit
    print("배팅한 금액은", b ,"입니다.")
    a = random.randint(1, 10)
    if a < 3:
        b *= 3
        bedgit += b
        return ("대박!! 3배의 보상을 얻으셨어요", '+', b)
    if a < 5:
        b *= 2
        bedgit += b
        return ("성공하셨습니다. 2배의 보상을 얻으셨어요", '+', b)
    else:
        bedgit -= b
        return ("아 아쉽네요.. \n", -b)
        

YeahSan()
batting()
print(gamble())
print(bedgit)

#박겨털 겨털 깍아라 