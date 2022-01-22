# N을 소인수분해
# N이 1 이면 아무것도 출력하지 않음
import sympy

# 나눌 수가 소수가 될 때까지 계속 소수로만 나누어야 함
# 마지막 남은 수가 엄청 큰 소수여도 끝나야 함 - 결과적으로 나눠질 수가 소수인지 아닌지 판단 하는 조건문이 필요할 것 - 어떻게?
#
def factorization(N):
    i = 2
    while N > 1 :
        if N % i == 0:
            N /= i
            print(i)
        else:
            i+=1


input1 = int(input())
factorization(input1)