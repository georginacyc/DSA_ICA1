# Name: Georgina Chew
# Admin No.: 180954W
# Tutorial Group: 2
# Phase 4: Challenge Question on Algorithm(5%)

# Lesson(s) learnt:
#   - sorting algorithms can be adapted for this purpose

def pairSum(seq, z):
    X = "not found"
    Y = "not found"
    t = False
    if z < seq[0] or z > (seq[-1] + seq[-2]):
        print("X =", X)
        print("Y =", Y)
        return t
    else:
        n = len(seq)

        for i in range(1, n):
            value = seq[i]
            pos = i
            while pos > 0:
                if value + seq[pos-1] != z:
                    pos -=1
                else:
                    X = value
                    Y = seq[pos-1]
                    t = True
                    break
        print("X =", X)
        print("Y =", Y)
        return t

s = [2, 3, 5, 7, 8, 10, 15, 16, 23, 28]

print(pairSum(s, 25))
