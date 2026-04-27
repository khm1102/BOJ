#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, k, p;
    scanf("%d %d %d", &n, &k, &p);

    vector<int> ranks(n);
    for (int i = 0; i < n; ++i)
        scanf("%d", &ranks[i]);


    if (n == 0)
    {
        printf("1\n");
        return 0;
    }

    if (n == p && ranks[n - 1] >= k)
    {
        printf("-1\n");
        return 0;
    }

    int left = 0, right = n - 1, rank = n + 1;
    while (left <= right)
    {
        int mid = left + (right - left) / 2;
        if (ranks[mid] > k)
            left = mid + 1;
        else {
            rank = mid + 1;
            right = mid - 1;
        }
    }

    printf("%d\n", rank);
    return 0;
}
