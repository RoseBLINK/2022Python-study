class microwave():
    def __init__(self):
        self.A = 300
        self.B = 60
        self.C = 10
        self.Acount = 0
        self.Bcount = 0
        self.Ccount = 0

    def count(self, T):
        # T에서 C 버튼을 제외한 A, B 버튼만큼의 시간을 뺐을때 0보다 크면 A를 빼고 있던 중에는 A를 계속 빼고
        # B를 빼고 있던 중에는 B를 계속 빼고, A 와 B 중 하나를 뺐는데 음수가 되면 다음 조건으로 넘어가야함.
        # 단, C를 뺐을때 음수가 나오면 -1 출력
        while T - self.A >= 0:
            T -= self.A
            self.Acount += 1

        if T == 0:
            print(self.Acount, self.Bcount, self.Ccount)
            return
        elif T < self.A:
            while T - self.B >= 0:
                T -= self.B
                self.Bcount += 1
            if T == 0:
                print(self.Acount, self.Bcount, self.Ccount)
                return
            elif T < self.B:
                while T - self.C >= 0:
                    T -= self.C
                    self.Ccount += 1
                if T == 0:
                    print(self.Acount, self.Bcount, self.Ccount)
                    return
                elif T < self.C:
                    print(-1)

num = int(input())
A = microwave()
A.count(num)