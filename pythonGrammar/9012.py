
# [[]]]

def solve(str):
    stack = []
    dic = {'{': '}', '[': ']','(': ')' }
    for i in range(len(str)):
        if str[i] in ["{","[","("]:
            stack.append(str[i])
        elif str in ["}","]",")"]:
            if len(str) == 0 :
                return False
            element = stack.pop(len(str)-1)
            if dic[element] != str[i]:
                return False
    return True

if __name__ == "__main__":
    str = input()
    if solve(str):
        print("true")
    else:
        print("false")

