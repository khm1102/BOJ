def r2a(roman):
    rd = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    a = 0
    p = 0
    for c in reversed(roman):
        v = rd[c]
        if v < p:
            a -= v
        else:
            a += v
        p = v
    return a

def a2r(arabic):
    ard = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
           50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    r = ''
    for v in sorted(ard.keys(), reverse=True):
        while arabic >= v:
            r += ard[v]
            arabic -= v
    return r

def add_rn(r1, r2):
    a1 = r2a(r1)
    a2 = r2a(r2)
    ta = a1 + a2
    tr = a2r(ta)
    return ta, tr

r1 = input().strip()
r2 = input().strip()

ta, tr = add_rn(r1, r2)
print(ta)
print(tr)
