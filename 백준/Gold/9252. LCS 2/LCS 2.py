import sys

def find_lcs(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    lcs_length = dp[n][m]
    
    lcs = []
    i, j = n, m
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    lcs = ''.join(reversed(lcs))
    
    return lcs_length, lcs

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

lcs_length, lcs = find_lcs(s1, s2)
sys.stdout.write(str(lcs_length) + '\n')
if lcs_length > 0:
    sys.stdout.write(lcs + '\n')
