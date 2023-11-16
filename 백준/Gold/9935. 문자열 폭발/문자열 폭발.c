#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 1000001

char str[MAX];
char bomb[MAX];
char result[MAX];
int top, bombLen;

int main() {
    scanf("%s %s", str, bomb);
    bombLen = strlen(bomb);

    int strLen = strlen(str);

    for (int i = 0; i < strLen; ++i) {
        result[top++] = str[i];
        
        if (result[top - 1] == bomb[bombLen - 1]) { 
            if (top - bombLen < 0) continue; 
            int same = 1;
            for (int j = 0; j < bombLen; ++j) {
                if (result[top - bombLen + j] != bomb[j]) {
                    same = 0;
                    break;
                }
            }
            if (same) top -= bombLen; 
        }
    }

    if (top == 0) printf("FRULA\n");
    else {
        result[top] = '\0';
        printf("%s\n", result);
    }

    return 0;
}
