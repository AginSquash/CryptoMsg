import random

def GetRandomCode(length):
    i = 0
    code = ""
    while i < length:
        code = code + str(random.randint(0,9))
        i=i+1
    return code

if __name__ == "__main__":
    print(GetRandomCode(6))