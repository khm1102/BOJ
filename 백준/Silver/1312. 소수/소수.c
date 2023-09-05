#include <stdio.h>

int main() {
    double a, b;
    int n;
    scanf("%lf %lf %d", &a, &b, &n);
    
    int q = a / b; 
    int i;
    for (i = 0; i < n; i++) { 
        a = (a - b * q) * 10;
        q = a / b;
    }
    
    printf("%d\n", q); 
    return 0;
}
