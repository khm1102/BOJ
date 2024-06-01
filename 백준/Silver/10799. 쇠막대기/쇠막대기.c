#include <stdio.h>
#include <string.h>

#define MAX_LEN 100001

int main() {
    char input[MAX_LEN];
    int stack = 0;   
    int res = 0;  

    scanf("%s", input);

    int length = strlen(input);

    for (int i = 0; i < length; i++) {
        if (input[i] == '(') {
            stack++;
        } else {  
            stack--; 
            if (input[i - 1] == '(') {
                res += stack;
            } else {
                res++;
            }
        }
    }

    printf("%d\n", res);

    return 0;
}
