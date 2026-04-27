
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define STR_SIZE 26

struct TrieNode
{
    int isEnd;
    int childCnt;

    struct TrieNode* child[STR_SIZE];
};

struct TrieNode *createNode()
{
    struct TrieNode* newNode = (struct TrieNode*)malloc(sizeof(struct TrieNode));
    if (newNode)
    {
        newNode -> isEnd = 0;
        newNode -> childCnt  = 0;
        memset(newNode-> child, 0, sizeof(newNode->child));
    }
    return newNode;
}

void insert(struct TrieNode* root, char* key)
{
    struct TrieNode* current = root;
    int len = strlen(key);

    for (int i = 0; i < len; i++)
    {
        int index = key[i] - 'a';

        if (!current -> child[index])
        {
            current -> child[index] = createNode();
            current -> childCnt++;
        }
        current = current -> child[index];

    }
    current -> isEnd =1;
}




void dfs(struct TrieNode* root, int* sum, int cnt){
    if (root -> isEnd)
        *sum += cnt;

    if (root -> childCnt == 0 || cnt == 0 || root -> isEnd || root -> childCnt > 1)
        cnt ++;

    for (int i = 0; i < STR_SIZE; i++)
    {
        if(root -> child[i])
            dfs(root -> child[i], sum, cnt);
    }

}
void delTrie(struct TrieNode* root)
{
    if (!root)
        return;

    for (int i = 0; i < STR_SIZE; i++)
    {
        if (root -> child[i])
            delTrie(root->child[i]);
    }

    free(root);
}

int main()
{
    int n;
    while(scanf("%d",&n) != EOF)
    {
        struct TrieNode* root = createNode();

        for (int i = 0; i < n; i++)
        {
            char s[100];
            scanf("%s", s);
            insert(root,s);
        }

        int sum = 0 ;
        dfs(root, &sum, 0);
        printf("%.2lf\n", (double) sum / n);
        delTrie((root));


    }
    return 0;
}