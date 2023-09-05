#include <stdio.h>

int main()
{
    int a, b, c;
    scanf("%d %d %d",&a,&b,&c);
    
    int min = 60 * a + b;
    min+=c;
    int hour = (min / 60) % 24;
    int minute = min % 60;
    printf("%d %d",hour , minute);

    return 0;
}
