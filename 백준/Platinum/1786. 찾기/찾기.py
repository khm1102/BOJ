
def compute_lps_array(pattern):
    length = 0
    i = 1
    lps = [0] * len(pattern)

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp(text, pattern):
    pos = []
    m = len(pattern)
    n = len(text)
    lps = compute_lps_array(pattern)
    i, j = 0, 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            pos.append(i - j + 1)
            j = lps[j - 1]

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return pos

def main():
	t = str(input())
	p = str(input())
	res = kmp(t, p)
	
	print(len(res), '\n'.join(map(str, res)), sep='\n')

if __name__ == '__main__':
    main()