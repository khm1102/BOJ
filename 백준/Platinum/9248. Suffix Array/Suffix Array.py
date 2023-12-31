def suffix_arr(s):
    n = len(s)
    rank = [ord(c) - ord('a') for c in s]
    temp = [0] * n
    sa = list(range(n))

    def arr_sort(k):
        sa.sort(key=lambda x: (rank[x], rank[x + k] if x + k < n else -1))

    k = 1
    while k < n:
        arr_sort(k)
        temp[sa[0]] = 0
        for i in range(1, n):
            left, right = (rank[sa[i - 1]], rank[sa[i - 1] + k] if sa[i - 1] + k < n else -1), (rank[sa[i]], rank[sa[i] + k] if sa[i] + k < n else -1)
            temp[sa[i]] = temp[sa[i - 1]] + (left != right)
        rank, temp = temp, rank
        k <<= 1

    return sa

def lcp_arr(s, sa):
    n = len(s)
    rank = [0] * n
    lcp = [0] * n
    for i in range(n):
        rank[sa[i]] = i
    k = 0
    for i in range(n):
        if rank[i] == n - 1:
            k = 0
            continue
        j = sa[rank[i] + 1]
        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k += 1
        lcp[rank[i]] = k
        if k:
            k -= 1
    return lcp

def main():
    s = input()
    sa = suffix_arr(s)
    print(' '.join(map(str, [x + 1 for x in sa])))

    lcp = lcp_arr(s, sa)
    print("x", ' '.join(map(str, lcp[:-1])))

if __name__ == "__main__":
    main()
