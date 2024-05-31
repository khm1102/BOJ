#include <stdio.h>
#include <string.h>

int main() {
    int n, k;
    char m[1000000];
    
    scanf("%d", &n);
    scanf("%s", m);
    scanf("%d", &k);
    k = n - k;
    
    int t = 1;
    if (k < 0) k = 0;
    
    while (k < n) {
        if (m[k] == '1') {
            t = 0;
            break;
        }
        k++;
    }
    
    printf("%s\n", t ? "YES" : "NO");
    
    return 0;
}
