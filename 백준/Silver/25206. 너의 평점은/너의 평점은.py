gp = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

t_c, t_gp = 0, 0.0

for _ in range(20):
    s, c, g = input().split()
    c = float(c)
    if g != "P":
        t_c += c
        t_gp += c * gp[g]

if t_c == 0:fg = 0.0
else:fg = t_gp / t_c

print("{:.6f}".format(fg))
