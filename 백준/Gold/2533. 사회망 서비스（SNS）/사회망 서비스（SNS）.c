#include <stdio.h>
#include <stdlib.h>

#define MOD 1000001

typedef struct Node
{
    int vertex;
    struct Node* next;
} Node;

Node* adj[MOD];
int dp[MOD][2];
int visited[MOD];

void add_edge(int u, int v) 
{
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->vertex = v;
    newNode->next = adj[u];
    adj[u] = newNode;
}

void dfs(int node) 
{
    visited[node] = 1;
    dp[node][0] = 1;
    dp[node][1] = 0;

    for (Node* neighbor = adj[node]; neighbor != NULL; neighbor = neighbor->next) 
    {
        if (!visited[neighbor->vertex]) 
        {
            dfs(neighbor->vertex);
            dp[node][0] += (dp[neighbor->vertex][0] < dp[neighbor->vertex][1]) ? dp[neighbor->vertex][0] : dp[neighbor->vertex][1];
            dp[node][1] += dp[neighbor->vertex][0];
        }
    }
}

int main() {
    int n;
    scanf("%d", &n);

    for (int i = 0; i < n - 1; i++) 
    {
        int u, v;
        scanf("%d %d", &u, &v);
        add_edge(u, v);
        add_edge(v, u);
    }

    dfs(1);

    int res = (dp[1][0] < dp[1][1]) ? dp[1][0] : dp[1][1];
    printf("%d\n", res);


    for (int i = 1; i <= n; i++) 
    {
        Node* current = adj[i];
        while (current != NULL) 
        {
            Node* next = current->next;
            free(current);
            current = next;
        }
    }

    return 0;
}
