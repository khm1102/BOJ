#include <stdio.h>

#define MAX 32

int main() {
    int n, k, m;
    scanf("%d %d %d", &n, &k, &m);

    int start_num[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &start_num[i]);
        start_num[i]--;
    }

    int parent[MAX][k];
    for (int i = 0; i < k; i++) {
        scanf("%d", &parent[0][i]);
        parent[0][i]--;
    }

    for (int level = 1; level < MAX; level++) {
        for (int j = 0; j < k; j++) {
            parent[level][j] = parent[level - 1][parent[level - 1][j]];
        }
    }

    for (int i = 0; i < n; i++) {
        int curr = start_num[i];
        int steps = m - 1;

        for (int level = 0; level < MAX; level++) {
            if (steps & (1 << level)) {
                curr = parent[level][curr];
            }
        }
        printf("%d ", curr + 1);
    }

    return 0;
}
