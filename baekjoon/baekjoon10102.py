#입력은 총 두 줄로 이루어져 있다. 첫째 줄에는 심사위원의 수 V (1 ≤  V ≤  15)가 주어지고,
# 둘째 줄에는 각 심사위원이 누구에게 투표했는지가 주어진다. A와 B는 각각 그 참가자를 나타낸다.

def vote(num, votes):

    if num == len(votes):

        countA = 0
        countB = 0
        listOfVote = list(votes)

        i = 0
        while i < len(votes):
            if listOfVote[i] == "A":
                countA += 1
            elif listOfVote[i] == "B":
                countB += 1
            i+=1
        if countA == countB:
            print("Tie")
        elif countA > countB:
            print("A")
        else:
            print("B")

    else:
        return

input1 = int(input())
input2 = input()

A = vote(input1, input2)