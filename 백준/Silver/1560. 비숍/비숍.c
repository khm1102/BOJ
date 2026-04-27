#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* add(char* a, char* b) {
    int len_a = strlen(a);
    int len_b = strlen(b);
    int max_len = len_a > len_b ? len_a : len_b;
    int carry = 0, sum;

    char* res = (char*)malloc(max_len + 2);
    res[max_len + 1] = '\0';

    int i = len_a - 1, j = len_b - 1, k = max_len;

    while (i >= 0 || j >= 0 || carry) {
        int digit_a = i >= 0 ? a[i--] - '0' : 0;
        int digit_b = j >= 0 ? b[j--] - '0' : 0;
        sum = digit_a + digit_b + carry;
        res[k--] = (sum % 10) + '0';
        carry = sum / 10;
    }

    if (k == 0)
        memmove(res, res + 1, max_len + 1);

    return res;
}

char* sub2(char* a) {
    int len = strlen(a);
    char* res = (char*)malloc(len + 1);
    strcpy(res, a);

    int i = len - 1, carry = 2;

    while (i >= 0 && carry > 0) {
        int digit = res[i] - '0';
        digit -= carry;
        if (digit < 0) {
            digit += 10;
            carry = 1;
        } else {
            carry = 0;
        }
        res[i--] = digit + '0';
    }

    if (res[0] == '0')
        memmove(res, res + 1, len);

    return res;
}

int main() {
    char n[71];
    scanf("%70s", n);

    if (strcmp(n, "1") == 0) {
        printf("1\n");
        return 0;
    }

    char* double_n = add(n, n);
    char* res = sub2(double_n);
    printf("%s\n", res);
    free(double_n);
    free(res);

    return 0;
}
