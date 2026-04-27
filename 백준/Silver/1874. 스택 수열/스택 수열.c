#include <stdio.h>

typedef struct Node {
    int value;
    struct Node* next;
} Node;

typedef struct {
    Node* top;
    Node nodes[100000];
    int nodeIdx;
} Stack;

void initStack(Stack* stack) {
    stack->top = NULL;
    stack->nodeIdx = 0;
}

void pushToStack(Stack* stack, int data, char* output, int* outIdx) {
    if (stack->nodeIdx < 100000) {
        Node* newNode = &stack->nodes[stack->nodeIdx++];
        newNode->value = data;
        newNode->next = stack->top;
        stack->top = newNode;

        output[(*outIdx)++] = '+';
    } else {
        exit(0);
    }
}

void popFromStack(Stack* stack, char* output, int* outIdx) {
    if (stack->top == NULL) {
        printf("NO");
        exit(0);
    }

    Node* temp = stack->top;
    stack->top = stack->top->next;

    output[(*outIdx)++] = '-';
}

int main() {
    int n, input, last = 0, outIdx = 0;
    char output[200000];

    scanf("%d", &n);

    Stack stack;
    initStack(&stack);

    for (int i = 0; i < n; i++) {
        scanf("%d", &input);

        while (last < input) {
            pushToStack(&stack, ++last, output, &outIdx);
        }

        if (stack.top != NULL && stack.top->value == input) {
            popFromStack(&stack, output, &outIdx);
        } else {
            printf("NO");
            return 0;
        }
    }

    for (int i = 0; i < n * 2; i++) {
        printf("%c\n", output[i]);
    }

    return 0;
}
