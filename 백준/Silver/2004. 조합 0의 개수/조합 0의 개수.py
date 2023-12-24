def tf_count(x):
    t_cnt = 0
    f_cnt = 0

    i = 2
    while i <= x:
        t_cnt += x // i
        i *= 2

    i = 5
    while i <= x:
        f_cnt += x // i
        i *= 5

    return t_cnt, f_cnt

n, m = map(int, input().split())
fc_n = tf_count(n)
fc_nm = tf_count(n - m)
fc_m = tf_count(m)

a = fc_n[0] - (fc_nm[0] + fc_m[0])
b = fc_n[1] - (fc_nm[1] + fc_m[1])

print(min(a, b))
