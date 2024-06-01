#include <stdio.h>
#include <string.h>

#define MOD 100001

void reverse(char *start, char *end) {
    while (start < end) {
        char temp = *start;
        *start = *end;
        *end = temp;
        start++;
        end--;
    }
}

int main() {
    char input[MOD];
    fgets(input, sizeof(input), stdin);

    int length = strlen(input);
    if (input[length - 1] == '\n') {
        input[length - 1] = '\0';
        length--;
    }

    char *start = NULL;
    for (int i = 0; i < length; i++) {
        if (input[i] == '<') {
            if (start) {
                reverse(start, &input[i - 1]);
                start = NULL;
            }
            while (i < length && input[i] != '>') {
                i++;
            }
        } else if (input[i] == ' ') {
            if (start) {
                reverse(start, &input[i - 1]);
                start = NULL;
            }
        } else {
            if (!start) {
                start = &input[i];
            }
        }
    }

    if (start) 
        reverse(start, &input[length - 1]);
    

    printf("%s\n", input);

    return 0;
}
