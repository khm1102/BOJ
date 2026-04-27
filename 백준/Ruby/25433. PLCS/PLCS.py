from math import sqrt

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def process_lcs_with_bitset(s1, s2):
    D = 0
    Match = [0] * 26

    for i, char in enumerate(s2):
        Match[ord(char) - ord('a')] |= 1 << i

    for char in s1:
        x = Match[ord(char) - ord('a')] | D
        y = (D << 1) | 1

        D = x ^ (x & (x - y))

    return bin(D).count('1')


def main():
    s = input()
    t = input()
    x = input()
    y = input()

    s = s.replace(y, '')
    t = t.replace(y, '')

    pos_s = s.find(x)
    pos_t = t.find(x)

    s1 = s[:pos_s]
    s2 = s[pos_s + 1:]
    t1 = t[:pos_t]
    t2 = t[pos_t + 1:]

    ret1 = process_lcs_with_bitset(s1, t1)
    ret2 = process_lcs_with_bitset(s2, t2)

    for i in range(ret1 + ret2 + 1, -1, -1):
        if is_prime(i):
            print(i)
            return

    print(-1)


if __name__ == "__main__":
    main()
