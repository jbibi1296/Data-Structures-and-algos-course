# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    x = True
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append((i+1,next))
        if next in ")]}":
            if len(opening_brackets_stack)==0:
                return i+1
            x = are_matching(opening_brackets_stack[-1][1],next)
            if x == False:
                return i+1
            else:
                opening_brackets_stack.pop(-1)
    if len(opening_brackets_stack)>0:
        return opening_brackets_stack[-1][0]
    return "Success"



def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
