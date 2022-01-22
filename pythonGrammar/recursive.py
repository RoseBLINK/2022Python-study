def fibo(n):
    # 1 1 2 3 5 8 13 21 34 ...
    # 1 2 3 4 5 6 7  8  9
    i = 1
    prevk = 1
    k = 1

    while i <= n :
        if i == 1 or i == 2:
            i+=1
            continue
        else:
            temp = k
            k = k + prevk
            prevk = temp
        i += 1
    return k

def fiboiter(n):
    arr = []
    for i in range(n+1):
        arr.append(0)
    arr[1] = 1
    arr[2] = 1

    for i in range (3,n+1):
        arr[i] = arr[i-1] + arr[i-2]

    return arr[n]

def fiboRecur(n):
    if n == 1 or n == 2:
        return 1
    return fiboRecur(n-1) + fiboRecur(n-2)


if __name__ == "__main__":
    print(fibo(100000))
    print(fibo(100000))
    print(fiboiter(100000))
    print(fiboiter(100000))
    print(fiboRecur(100))
    print(fiboRecur(100))