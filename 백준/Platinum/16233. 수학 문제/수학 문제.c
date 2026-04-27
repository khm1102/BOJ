#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);

    while (t--) {
        int n;
        scanf("%d", &n);

        if (n % 9 != 0) {
            printf("-1 ");
            continue;
        }

        int r = 999999999;
        int x = 0;
        
        while (r) {
            if (9 < (n / r)) {
                printf("-1 ");
                break;
            }
            x = (x + n / r) * 10;
            n %= r;
            r /= 10;
        }

        if (r == 0) {
            printf("%d ", x);
        }
    }

    return 0;
}
