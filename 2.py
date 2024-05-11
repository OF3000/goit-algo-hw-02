from collections import deque

def is_pol(s):
    str=''.join([ch.lower() for ch in s if ch.isalpha()])

    dq= deque(str)

    while len(dq)>1:
        if dq.pop() != dq.popleft():
            return False
    return True


if __name__ == "__main__": 

    str = input("Input string: ")
    print(is_pol(str))
