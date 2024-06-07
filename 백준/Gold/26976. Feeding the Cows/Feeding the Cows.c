#include <stdio.h>
#include <string.h>

#define MAXN 100000

int main() {
    int t;
    scanf("%d", &t);

    while (t--) {
        int n, k;
        char s[MAXN + 1];
        char ans[MAXN + 1];
        scanf("%d %d", &n, &k);
        scanf("%s", s);

        for (int i = 0; i < n; ++i) {
            ans[i] = '.';
        }
        ans[n] = '\0';

        int cnt = 0;
        int g = -1, h = -1;

        for (int i = 0; i < n; ++i) {
            if ((s[i] == 'G' && i <= g) || (s[i] == 'H' && i <= h)) {
                continue;
            }

            int found = 0;
            for (int j = i + k < n ? i + k : n - 1; j >= (i - k > 0 ? i - k : 0); --j) {
                if (ans[j] == '.') {
                    ans[j] = s[i];
                    cnt++;
                    found = 1;
                    if (s[i] == 'G') g = i + 2 * k;
                    if (s[i] == 'H') h = i + 2 * k;
                    break;
                }
            }
            
            if (!found) {
                if (s[i] == 'G') g = i + 2 * k;
                if (s[i] == 'H') h = i + 2 * k;
            }
        }
        printf("%d\n", cnt);
        printf("%s\n", ans);
    }

    return 0;
}
