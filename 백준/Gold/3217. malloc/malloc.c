#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MEMORY_SIZE 100000
#define VAR_SIZE 1000

typedef struct Node {
    int start;
    int size;
    struct Node* next;
} Node;

Node* free_list = NULL;
int var_table[VAR_SIZE]; 
int var_size_table[VAR_SIZE]; 
char var_names[VAR_SIZE][5]; 
int var_count = 0; 

void init_memory() {
    free_list = (Node*)malloc(sizeof(Node));
    free_list->start = 1;
    free_list->size = MEMORY_SIZE;
    free_list->next = NULL;
}

int find_var_index(const char* var_name) {
    for (int i = 0; i < var_count; i++) {
        if (strcmp(var_names[i], var_name) == 0) {
            return i;
        }
    }
    strcpy(var_names[var_count], var_name);
    var_table[var_count] = 0;
    var_size_table[var_count] = 0;
    return var_count++;
}

int malloc_memory(int size) {
    Node* current = free_list;
    Node* prev = NULL;

    while (current) {
        if (current->size >= size) {
            int alloc_start = current->start;
            current->start += size;
            current->size -= size;

            if (current->size == 0) {
                if (prev) {
                    prev->next = current->next;
                } else {
                    free_list = current->next;
                }
                free(current);
            }

            return alloc_start;
        }
        prev = current;
        current = current->next;
    }

    return 0;
}

void free_memory(int start, int size) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->start = start;
    new_node->size = size;
    new_node->next = NULL;

    if (!free_list || free_list->start > start) {
        new_node->next = free_list;
        free_list = new_node;
    } else {
        Node* current = free_list;
        while (current->next && current->next->start < start) {
            current = current->next;
        }
        new_node->next = current->next;
        current->next = new_node;
    }

    Node* current = free_list;
    while (current && current->next) {
        if (current->start + current->size == current->next->start) {
            Node* to_free = current->next;
            current->size += current->next->size;
            current->next = current->next->next;
            free(to_free);
        } else {
            current = current->next;
        }
    }
}

int main() {
    int N;
    scanf("%d", &N);
    char command[30];

    init_memory();

    for (int i = 0; i < N; i++) {
        scanf("%s", command);
        if (strstr(command, "malloc")) {
            char var_name[5];
            int size;
            sscanf(command, "%4s=malloc(%d);", var_name, &size);
            int var_index = find_var_index(var_name);
            int addr = malloc_memory(size);
            var_table[var_index] = addr;
            var_size_table[var_index] = addr ? size : 0; 
        } else if (strstr(command, "free")) {
            char var_name[5];
            sscanf(command, "free(%4s);", var_name);
            int var_index = find_var_index(var_name);
            if (var_table[var_index]) {
                free_memory(var_table[var_index], var_size_table[var_index]);
                var_table[var_index] = 0;
                var_size_table[var_index] = 0;
            }
        } else if (strstr(command, "print")) {
            char var_name[5];
            sscanf(command, "print(%4s);", var_name);
            int var_index = find_var_index(var_name);
            printf("%d\n", var_table[var_index]);
        }
    }

    return 0;
}
