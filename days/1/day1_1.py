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
    if False
    else open("day1.txt").read()
).strip().split("\n")

cur = 50
res = 0
for i in IN:
    dir = i[0]

    if dir == "L":
        cur -= int(i[1:])
        if cur < 0:
            cur = (100-abs(cur)) % 100
    else:
        cur += int(i[1:])
        cur = cur % 100

    if cur == 0: res += 1

print(res)





