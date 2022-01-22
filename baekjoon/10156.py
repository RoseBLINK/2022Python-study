# 과자 한개 가격: K
# 사려고 하는 과자 개수: N
# 현재 가진 돈의 액수: M
# 받아야하는 모자란 돈의 액수?
# 인풋은 띄어쓰기로 구분

def getMoney(input):

    list = input.split(' ')
    getMoney = int(list[0]) * int(list[1]) - int(list[2])
    if getMoney < 0:
        print("0")
    else:
        print(getMoney)

input1 = input()
getMoney(input1)