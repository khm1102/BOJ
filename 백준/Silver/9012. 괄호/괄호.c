// 서울 디지텍고등학교 1학년 2학기 자료구조 수업 중 풀었던 문제.

#include <stdio.h>
#include <stdlib.h>

// 링크드 리스트 노드 구조체
typedef struct Node {
    char data;
    struct Node* next;
} Node;

// 링크드 리스트 초기화
void initList(Node** head) {
    *head = NULL;
}

// 링크드 리스트가 비어있는지 확인
int isEmpty(Node* head) {
    return (head == NULL);
}

// 링크드 리스트에 데이터 삽입
void insert(Node** head, char data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;

    if (*head == NULL) {
        *head = newNode;
    } else {
        Node* temp = *head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = newNode;
    }
}

// 링크드 리스트에서 마지막 노드 삭제
void removeLast(Node** head) {
    if (*head == NULL) {
        exit(EXIT_FAILURE);
    } else if ((*head)->next == NULL) {
        free(*head);
        *head = NULL;
    } else {
        Node* prev = NULL;
        Node* curr = *head;
        while (curr->next != NULL) {
            prev = curr;
            curr = curr->next;
        }
        free(curr);
        prev->next = NULL;
    }
}
char* checkVPS(char* str) {
    Node* list = NULL;
    initList(&list);

    while (*str) {
        if (*str == '(') {
            insert(&list, *str);
        } else if (*str == ')') {
            if (isEmpty(list)) {
                return "NO";
            }
            removeLast(&list);
        }
        str++;
    }

    if (isEmpty(list)) {
        return "YES";
    } else {
        return "NO";
    }
}

int main() {
    int T;
    scanf("%d", &T);

    while (T--) {
        char str[51];
        scanf("%s", str);
        printf("%s\n", checkVPS(str));
    }

    return 0;
}
