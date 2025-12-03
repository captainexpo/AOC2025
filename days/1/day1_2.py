IN = (
    """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
    """.strip()
    if len(__import__("sys").argv) >= 2
    else open("day1.txt").read()
).strip().split("\n")

cur = 50
during = 0
final = 0
for i in IN:
    dir = i[0]

    v = int(i[1:])
    if dir == "L":
        for k in range(v):
            cur -= 1
            if k != v-1 and cur == 0: during += 1
            if cur < 0: cur = 100-abs(cur)
        if cur == 0:
            final += 1
    else:
        for k in range(v):
            cur += 1
            cur %= 100
            if k != v-1 and cur == 0: during += 1
        if cur == 0:
            final += 1

print(during, final, during + final)





