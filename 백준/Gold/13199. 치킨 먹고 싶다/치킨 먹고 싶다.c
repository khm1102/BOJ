#include <stdio.h>

int main() {
    int T;
    scanf("%d", &T);

    for (int i = 0; i < T; i++) {
        int P, M, F, C;
        scanf("%d %d %d %d", &P, &M, &F, &C);

        if (C * (M / P) > F) {
            printf("%d\n", (C * (M / P) - C) / (F - C) - C * (M / P) / F);
        } else {
            printf("0\n");
        }
    }

    return 0;
}
