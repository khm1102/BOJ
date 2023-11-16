#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

typedef struct Queue {
    Node* front;
    Node* rear;
    int size;
} Queue;

Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

void initializeQueue(Queue* queue) {
    queue->front = queue->rear = NULL;
    queue->size = 0;
}

void enqueue(Queue* queue, int data) {
    Node* newNode = createNode(data);
    if (queue->rear == NULL) {
        queue->front = queue->rear = newNode;
    } else {
        queue->rear->next = newNode;
        queue->rear = newNode;
    }
    queue->size++;
}

int dequeue(Queue* queue) {
    if (queue->front == NULL) {
        return -1; 
    } else {
        int data = queue->front->data;
        Node* temp = queue->front;
        queue->front = queue->front->next;
        free(temp);
        if (queue->front == NULL) {
            queue->rear = NULL;
        }
        queue->size--;
        return data;
    }
}

void solve(int N, int K) {
    Queue queue;
    initializeQueue(&queue);

    for (int i = 1; i <= N; ++i) {
        enqueue(&queue, i);
    }

    printf("<");
    while (queue.size > 1) {
        for (int i = 0; i < K - 1; ++i) {
            int data = dequeue(&queue);
            enqueue(&queue, data);
        }
        printf("%d, ", dequeue(&queue));
    }
    printf("%d>\n", dequeue(&queue));
}

int main() {
    int N, K;
    scanf("%d %d", &N, &K);
    solve(N, K);
    return 0;
}
