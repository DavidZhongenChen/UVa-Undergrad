S = input()
P = input()
def call_this():
    if S == P:
        return True
    if S[0:-1] == P and S[-1].isnumeric():
        return True
    if S[1:] == P and S[0].isnumeric():
        return True
    if S == P.swapcase():
        return True
    return False

if call_this() == True:
    print("Yes")
else:
    print("No")

